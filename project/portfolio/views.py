from django.views.generic import View
from game.models import *
from django.shortcuts import render, redirect
from portfolio.models import Portfolio, Holding, Stock_history, Stocks_Tracked
from portfolio.forms import portfolio_form, holding_form
from django.utils.text import slugify
from django.contrib.auth.models import User
from pprint import pprint as print
import portfolio.portfolio as p
from django.http import HttpResponse

## nothing about game belongs in this file
class Display_all( View ):
    def get( self, request ):
        if request.user.is_anonymous():

            return redirect( '/' )
        
        user_id = request.GET.get( 'user_id', request.user.id )
        request.context_dict[ 'portfolios' ] = p.Portfolio.by_user_id( None, user_id )
        
        return render( request, 'portfolio/display_all.html', request.context_dict )

class Create( View ):
    def get( self, request ):
        if request.user.is_anonymous():
            
            return redirect( '/' )

        request.context_dict[ 'form' ] = p.Portfolio.create_form()
        
        return render( request, 'portfolio/create.html', request.context_dict )

    def post( self, request ):
        form = p.Portfolio.create_form( request.POST )
        results = p.Portfolio.create( form, request.user.id )
        if results:

            return redirect( '/portfolio/{}/manage'.format( results.slug ) )

        request.context_dict[ 'form' ] = form
        
        return render( request, 'portfolio/create.html', request.context_dict )


class Manage( View ):
    def get( self, request, slug ):
        request.context_dict[ 'portfolio' ] = p.Portfolio( slug )
        request.context_dict[ 'slug' ] = slug

        return render( request, 'portfolio/manage.html', request.context_dict )

# needs to be converted to portfolio.py 
class Holding_add( View ):
    def get( self, request, slug ):
        request.context_dict[ 'portfolio' ] = p.Portfolio( slug )
        request.context_dict[ 'slug' ] = slug
        request.context_dict[ 'form' ] = p.Portfolio.create_holding()
        current = request.session['current_date']
        stocks = Stock_history.objects.filter(date=current)
        return render( request, 'portfolio/holding_add.html', request.context_dict )

    def post( self, request, slug ):
        form = holding_form( request.POST )
        portfolio = p.Portfolio(slug)
        results = portfolio.add_holding( form, request.user.id )
        if results:

        # this logic was moved to portfolio
        # if form.is_valid():
        #     request
        #     data = form.cleaned_data
        #     data[ 'portfolio' ] = Portfolio.objects.get( slug=slug )
        #     data = Holding.objects.create( **data )

            return redirect( '/portfolio/{}/manage'.format( slug ) )
        else:
            request.context_dict[ 'form' ] = form
            request.context_dict[ 'slug' ] = slug
            request.context_dict[ 'error' ] = 'Invalid?'

            return render( request, 'portfolio/holding_add.html', request.context_dict )

class Holding_update( View ):
    def post(self,request,slug):
        portfolio = p.Portfolio(slug)
        portfolio.remove_holding(request)
        return redirect("/portfolio/"+slug+"/manage")

# needs to be converted to portfolio.py and template created
class Edit( View ):
    def get( self, request, slug ):
        request[ 'portfolio' ] = Portfolio.objects.get( slug=slug )
        request[ 'form' ] = portfolio_form( request[ 'portfolio' ] )
        
        return render( request, 'portfolio/edit.html', request.context_dict )

    def post( self, request, slug ):
        form = portfolio_form( request.POST )
        if form.is_valid():
            data = form.cleaned_data
            data[ 'slug' ] = slugify( request.POST[ 'title' ] )
            data = Post.objects.update( **data )

            return redirect( '/portfolio/{}'.format( data.slug ) )

        request.context_dict[ 'form' ] = portfolio_form( request.POST )
        request.context_dict[ 'error' ] = "Please review each field"
        
        return render( request, 'portfolio/create.html', request.context_dict )

class Tracked( View ):
    def get( self, request ):
        request.context_dict['tracked'] = Stocks_Tracked.objects.all()
        
        return render( request, 'portfolio/tracked.html', request.context_dict )


## not sure form here down

class Find_stock_by_name(View):
    def get(self, request):
        symbol = request.GET.get["symbol"]
        stock = Stock.objects.get(symbol=symbol, date__month=(request.session['game_round'] + 6) % 12)
        game_round = request.session['game_round']
        return render( request, 'game/round.html', {"game_round":game_round, 'user':request.session.user, 'price':stock.price, 'date':stock.date, 'symbol':stock.symbol})

#lot of overlap Buy_stock and Sell_shares, NOT DRY
class Buy_stock(View):
    def post(self, request):
        balance = request.POST['balance']
        symbol = request.POST['symbol']
        shares = int(request.POST['shares'])
        date = request.POST['date']
        stock = Stock.objects.get(symbol=symbol, date=date)
        price = stock.price
        balance = request.session['balance'] - (shares * price)
        request.session['balance'] = balance
        portfolio = Portfolio.objects.filter(user=request.user).order_by('date')[0]
        t = Transaction.objects.create(symbol=symbol, number_of_shares=shares, date_created=date, account_change=(shares * price * -1), portfolio=portfolio)
        s = Portfolio.objects.create(symbol=symbol, amount=shares, date_bought=date, price_bought=price, portfolio=portfolio)
        return redirect( 'game/round.html')


class Sell_shares(View):
    def post(self, request):
        balance = request.POST['balance']
        symbol = request.POST['symbol']
        shares = int(request.POST['shares'])
        date = request.POST['date']
        stock = Stock.objects.get(symbol=symbol, date=date)
        price = stock.price
        balance = request.session['balance'] + (shares * price)
        request.session['balance'] = balance        
        portfolio = Portfolio.objects.filter(user=request.user).order_by('date')[0]
        t = Transaction.objects.create(symbol=symbol, number_of_shares=shares, date_created=date, account_change=(shares * price), portfolio=portfolio)
        #this function will break if there are more than one entry for that stock, which is likely
        s = Portfolio.objects.get(symbol=symbol, portfolio=portfolio)
        s.amount -= shares 
        s.save()
        return redirect( 'game/round.html')
