from django.views.generic import View
from django.utils.text import slugify
from django.shortcuts import render, redirect
from django.forms.util import ErrorList

from game.forms import GameCreateForm
from game.models import *

from portfolio.models import Stock_history, Holding
from portfolio.portfolio import Portfolio

import datetime
from pprint import pprint
from types import MethodType

def incrementer(time_span):
    if time_span == "weekly":
        return 7
    elif time_span == "monthly":
        return 30
    else:
        return 365

def get_game( game_id ):

    game = Whole_Game.objects.get( id=game_id )
    setattr( game, 'portfolio', Portfolio( game.portfolio_id ) )
    game.change_date( game.current_date )

    return game

class CreateGame( View ):
    
    def get( self, request ):
        if request.user.is_anonymous():
            return redirect('/')
        request.context_dict['form'] = GameCreateForm()

        return render( request, 'game/index.html', request.context_dict )

    def post(self, request):
        form = GameCreateForm( request.POST )
        if form.is_valid():
            form_data = form.cleaned_data
            form_data['user'] = User.objects.get( id=request.user.id )
            form_data['balance'] = form_data['start_balance']

            portfolio_data = {
                'title': "game_{}".format( form_data['name'] ),
                'description': "Portfolio for game play.",
                'user': form_data['user']
            }

            portfolio = Portfolio.create( portfolio_data )

            form_data['portfolio_id'] = portfolio.id

            game = Whole_Game.objects.create( **form_data )
            return redirect( '/game/{}/start'.format( game.id ) )
        else:
            request.context_dict['form'] = form 
            return render( request, 'game/index.html', request.context_dict )


class UnfinishedGames( View ):
    
    def get(self, request):
        if request.user.is_anonymous():
            return redirect( '/')
        request.context_dict['games'] = Whole_Game.objects.filter(user=request.user, end_date=None)
        request.context_dict['starturl'] = "/game/{}/start"
        return render(request, 'game/find.html', request.context_dict)


class Start( View ):
    
    def get( self, request, game_id ):
        if request.user.is_anonymous():
            return redirect('/')
        request.session.set_expiry(300)
        game = get_game( game_id )
        request.session['game_id'] = game_id
        return redirect( '/game/{}/manage'.format( game_id ) )


class Manage( View ):
    
    def get( self, request, game_id ):
        if request.user.is_anonymous():
            return redirect('/')
        request.context_dict['game'] = get_game( game_id )
        request.context_dict['form'] = Portfolio.create_holding()

        return render( request, 'game/manage.html', request.context_dict )


class Manage_add( View ):
    def post( self, request, game_id ):
        request.context_dict['game'] = get_game( game_id )
        form = Portfolio.create_holding( request.POST )
        request.context_dict[ 'form' ] = form
        if form.is_valid():
            form_data = form.cleaned_data
            form_data['date'] = str( request.context_dict['game'].current_date )

            form_data['price'] = request.context_dict['game'].portfolio.stock_by_date( form_data['symbol'] ).close
            if form_data['price'] * form_data["shares"] <= request.context_dict["game"].balance:
                results = request.context_dict['game'].portfolio.add_holding( form_data )

                request.context_dict['game'].balance -= results
                request.context_dict['game'].save( update_fields=["balance"] )

                return redirect( '/game/{}/manage'.format( game_id ) )
            else:
                errors = request.context_dict[ 'form' ]._errors.setdefault("shares", ErrorList())
                errors.append(u"You cannot afford that")
                return render( request, 'game/manage.html', request.context_dict ) 
        else:
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
    
    def get(self, request, game_id):
        if request.user.is_anonymous():
            return redirect('/')
        game = get_game( game_id )
        if game.total_rounds == game.current_round:
            return redirect( "/game/" + game_id + "/endgame")
        game.current_round += 1
        game.current_date += datetime.timedelta(days=incrementer(game.game_type))
        game.current_date = game.change_date(game.current_date)
        game.save()   
        return redirect( '/game/{}/manage'.format( game_id ) )


class StatsView( View ):
    template_name = 'game/stats.html'

    def get(self, request, game_id ):
        game = get_game( game_id )
        if request.user.is_anonymous():
            return redirect('/')
        start = game.current_date - datetime.timedelta(days=incrementer(game.game_type))
        search_start = game.current_date - datetime.timedelta(days=7)
        stocks = Stock_history.objects.filter(date__range=[start, game.current_date])
        return render(request, self.template_name, {'stocks':stocks, 'game':game})


class Leaderboard(View):
    
    def get(self, request):
        if request.user.is_anonymous():
            return redirect( '/')
        else:
            request.context_dict['highscores'] = Whole_Game.objects.all().order_by('final_score')[:9]
            return render( request, 'game/leaderboard.html', request.context_dict)


class EndGame( View ):
    def get(self, request, game_id):
        if request.user.is_anonymous():
            return redirect('/')
        game = get_game( game_id )
        game.current_date += datetime.timedelta(days=incrementer(game.game_type))
        game.current_date = game.change_date(game.current_date)
        game.end_date = game.current_date
        for symbol,values in game.portfolio.stocks.items():
            price = game.portfolio.remove_holding( symbol, values["shares"] )
            game.balance += price
        game.final_score = game.balance
        game.save()
        request.context_dict["game"] = game
        return render (request, 'game/endgame.html', request.context_dict)
