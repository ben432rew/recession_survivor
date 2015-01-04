from django.views.generic import View
from django.utils.text import slugify
from django.shortcuts import render, redirect

from game.forms import GameCreateForm
from game.models import *

from portfolio.models import Stock_history, Holding
from portfolio.portfolio import Portfolio

import datetime
from pprint import pprint

def incrementer(time_span):
    if time_span == "weekly":
        return 7
    elif time_span == "monthly":
        return 30
    else:
        return 365

def get_game( game_id ):
    game = Whole_Game.objects.get( id=game_id )
    setattr( game, 'portfolio', Portfolio( game.portfolio ) )
    game.portfolio.chage_date( game.current_date )
    return game

class CreateGame( View ):
    def get( self, request ):
        request.context_dict['form'] = GameCreateForm()

        return render( request, 'game/index.html', request.context_dict )

    def post(self, request):
        form = GameCreateForm( request.POST )
        if form.is_valid():
            form_data = form.cleaned_data
            form_data['user'] = User.objects.get( id=request.user.id )

            portfolio_data = {
                'title': "game_{}".format( form_data['name'] ),
                'description': "Portfolio for game play.",
                'user': form_data['user']
            }

            portfolio = Portfolio.create( portfolio_data )

            form_data['current_round'] = 0

            form_data['portfolio'] = portfolio.id

            game = Whole_Game.objects.create( **form_data )
            return redirect( '/game/{}/start'.format( game.id ) )
        else:
            request.context_dict['form'] = form 
            return render( request, 'game/index.html', request.context_dict )


class Start( View ):
    def get( self, request, game_id ):
        game = get_game( game_id )
        request.session['game_id'] = game_id
        return redirect( '/game/{}/manage'.format( game_id ) )


class Manage( View ):
    def get( self, request, game_id ):
        request.context_dict['game'] = get_game( game_id )

        return render( request, 'game/manage.html', request.context_dict )


class Manage_add( View ):
    def post( self, request, game_id ):
        request.context_dict['game'] = get_game( game_id )
        form = Portfolio.create_holding( request.POST )

        # logic here to make sure user can afford stocks
        if form.is_valid():
            form_data = form.cleaned_data
            form_data['date'] = str( request.context_dict['game'].current_date )

            form_data['price'] = request.context_dict['game'].portfolio.stock_date( form_data['symbol'] ).close

            results = request.context_dict['game'].portfolio.add_holding( form_data )

            request.context_dict['game'].balance -= results
            request.context_dict['game'].save( update_fields=["balance"] )

            return redirect( '/game/{}/manage'.format( game_id ) )

        else:
            request.context_dict[ 'form' ] = form

            return render( request, 'game/manage.html', request.context_dict )


class Manage_remove( View ):
    def post( self, request, game_id ):
        game = get_game( game_id )
        symbol = request.POST.get( 'symbol', None )
        amount = request.POST.get( 'amount', None )
        results = game.portfolio.remove_holding( symbol, amount )

        if results:
            game.balance += results
            game.save( update_fields=["balance"] )

            return redirect( '/game/{}/manage'.format( game_id ) )
        else:
            # add error here, but this should never be called?
            return redirect( '/game/{}/manage'.format( game_id ) )


class RoundView( View ):
    template_name = 'game/round.html'
# the round is incremented by 1 every round, but the date could be incremented by 7 days, 30 days, or 365 days
# which actually doesn't work because it doesn't account for leap years, months not 30 days long and most importantly, THE USER CAN ONLY ACTUALLY PLAY ON WEEKDAYS NOT WEEKENDS OR HOLIDAYS
    def get(self, request):
        request.session.set_expiry(300)
        game = get_game( game_id )
        #add the round, update the date
        request.session['game_id'] = game_id
        return redirect( '/game/{}/manage'.format( game_id ) )


class UnfinishedGames( View ):
    template_name = 'game/find.html'

    def get(self, request):
        request.context_dict['games'] = Whole_Game.objects.filter(user=request.user, end_date=None)
        request.context_dict['starturl'] = "/game/{}/start"
        return render(request, self.template_name, request.context_dict)


class StatsView( View ):
    template_name = 'game/stats.html'

    def get(self, request):
        if request.session['game_type'] == 'weekly':
                days = request.session['round']*7
                start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
                time = datetime.timedelta(days=days)
                end = start + time
                search_start = end - datetime.timedelta(days=7)
                stocks = Stock_history.objects.filter(date__range=[search_start, end])
                game = Whole_Game.objects.get(id=request.session['game_id'])
                return render(request, self.template_name, {'stocks':stocks, 'game':game})
        elif request.session['game_type'] == 'monthly':
            days = request.session['round']*31
            start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
            time = datetime.timedelta(days=days)
            end = start + time
            search_start = end - datetime.timedelta(days=31)
            request.session['search_start'] = search_start
            request.session['current_date'] = end
            stocks = Stock.objects.filter(date__range=[search_start, end])
            return render(request, self.template_name, {'stocks':stocks})
        elif request.session['game_type'] == 'yearly':
            days = request.session['round']*365
            start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
            time = datetime.timedelta(days=days)
            end = start + time
            search_start = end - datetime.timedelta(days=365)
            request.session['search_start'] = search_start
            request.session['current_date'] = end
            stocks = Stock.objects.filter(date__range=[search_start, end])
            return render(request, self.template_name, {'stocks':stocks})
        else:
            pass
