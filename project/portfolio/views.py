from django.views.generic import View
from django.shortcuts import render

class Find_stock_by_name(symbol):
    def post(self, request):
        current = None
        return render( request, 'game/round.html', {"current":current}))
        #show all the users' current stocks owned

class Display_all():
    def post(self, request):
        current = None
        return render( request, 'game/round.html', {"current":current}))
        #show all the stocks there are to possible to buy, paginated

class Display_owned(portfolio):
    def post(self, request):
        current = None
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

