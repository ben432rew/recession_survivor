from django.views.generic import View
from django.shortcuts import render, redirect
from portfolio.models import Portfolio, Stock, Transaction, Stock_owned


class Find_stock_by_name(View):
    def get(self, request):
        symbol = request.GET.get["symbol"]
        stock = Stock.objects.get(symbol=symbol, date__month=(request.session['game_round'] + 6) % 12)
        game_round = request.session['game_round']
        return render( request, 'game/round.html', {"game_round":game_round, 'user':request.session.user, 'price':stock.price, 'date':stock.date, 'symbol':stock.symbol}))


class Display_all(View):
    def get(self, request):
        game_round = request.session['game_round']        
        all_stocks = Stock.objects.filter(date__month(request.session['game_round'] + 6) % 12)
        return render( request, 'game/round.html', {"game_round":game_round, "all_stocks":all_stocks, 'user':request.session.user}))


class Display_owned(View):
    def get(self, request):
        game_round = request.session['game_round']
        owned = Portfolio.objects.select_related('Stock_owned').filter(user=request.user)
        return render( request, 'game/round.html', {"game_round":game_round, "stock_owned":owned, 'user':request.session.user}))

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
        s = Stock_owned.objects.create(symbol=symbol, amount=shares, date_bought=date, price_bought=price, portfolio=portfolio)
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
        s = Stock_owned.objects.get(symbol=symbol, portfolio=portfolio)
        for shares in s:
            if 
        s.save()
        return redirect( 'game/round.html')
