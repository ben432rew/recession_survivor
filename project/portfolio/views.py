from django.views.generic import View
from django.shortcuts import render
from portfolio.models import Portfolio, Stock

class Find_stock_by_name(symbol):
    
    def post(self, request):
        user_obj = request.user
        # untested and unsure how to get current game stocks 
        info = Portfolio.objects.select_related('Stock_owned').filter(user=user_obj)
        current = info
        return render( request, 'game/round.html', {"current":current}))
        #show all the users' current stocks owned

class Display_all():
    
    def post(self, request):
        # untested
        all_stocks = Stock.objects.all()
        current = all_stocks
        return render( request, 'game/round.html', {"current":current}))
        #show all the stocks there are to possible to buy, paginated

class Display_owned(portfolio):
    
    def post(self, request):
        info = Portfolio.objects.select_related('Stock_owned').filter(user=user_obj)
        current = info
        return render( request, 'game/round.html', {"current":current}))
        #show all the users' current stocks owned

class Buy_stock(portfolio, symbol, shares):

    def post(self, request):
        current = None
        return render( request, 'game/round.html', {"current":current}))
        #buy shares of a stock

class Sell_shares(portfolio, symbol, shares):
    
    def post(self, request):
        current = None
        return render( request, 'game/round.html', {"current":current}))
        #sell shares of a stock

