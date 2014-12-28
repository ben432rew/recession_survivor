from django.views.generic import View
from django.shortcuts import render, redirect
from portfolio.models import Portfolio
from portfolio.forms import create_form
from django.utils.text import slugify
from django.contrib.auth.models import User

## nothing about game belongs in this file

class Create( View ):
    def get( self, request ):
        request.context_dict[ 'form' ] = create_form()
        return render( request, 'portfolio/create.html', request.context_dict )

    def post( self, request ):
        form = create_form( request.POST )
        if form.is_valid():
            data = form.cleaned_data
            data[ 'user' ] = User.objects.get( id=request.user.id )
            data[ 'slug' ] = slugify( request.POST['title'] )
            data = Portfolio.objects.create( **data )

            return redirect( '/portfolio/{}'.format( data.slug ) )

        request.context_dict[ 'form' ] = create_form( request.POST )
        request.context_dict[ 'error' ] = "Please review each field"
        return render( request, 'portfolio/create.html', request.context_dict )

class Edit( View ):
    def get( self, request, slug ):
        request[ 'portfolio' ] = Portfolio.objects.get( slug=slug )
        return render( request, 'portfolio/edit.html', request.context_dict )

    def post( self, request, slug ):
        form = create_form( request.POST )
        if form.is_valid():
            data = form.cleaned_data
            data[ 'slug' ] = slugify( request.POST['title'] )
            data = Post.objects.update( **data )

            return redirect( '/portfolio/{}'.format( data.slug ) )

        request.context_dict[ 'form' ] = create_form( request.POST )
        request.context_dict[ 'error' ] = "Please review each field"
        return render( request, 'portfolio/create.html', request.context_dict )

class Display_all( View ):
    def get( self, request ):
        get_user = request.GET.get( 'user_id', request.user.id )
        request.context_dict[ 'portfolios' ] = Portfolio.objects.filter( user = User.objects.get( id=request.user.id ) )
        print( request.context_dict['portfolios'] )
        return render( request, 'portfolio/display_all.html', request.context_dict )

class Find_stock_by_name(View):
    def get(self, request):
        symbol = request.GET.get["symbol"]
        stock = Stock.objects.get(symbol=symbol, date__month=(request.session['game_round'] + 6) % 12)
        game_round = request.session['game_round']
        return render( request, 'game/round.html', {"game_round":game_round, 'user':request.session.user, 'price':stock.price, 'date':stock.date, 'symbol':stock.symbol})

class Display_owned(View):
    def get(self, request):
        game_round = request.session['game_round']
        owned = Portfolio.objects.select_related('Portfolio').filter(user=request.user)
        return render( request, 'game/round.html', {"game_round":game_round, "portfolio":portfolio, 'user':request.session.user})

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
