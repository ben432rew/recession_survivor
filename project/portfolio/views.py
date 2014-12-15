from django.views.generic import View
from django.shortcuts import render
from portfolio.models import Portfolio, Stock

class Find_stock_by_name(View):
    def get(self, request):
        game_round = request.session['game_round']
        return render( request, 'game/round.html', {"game_round":game_round, 'user':request.session.user}))


class Display_all(View):
    def get(self, request):
        game_round = request.session['game_round']        
        if request.session['game_round'] > 6:
            all_stocks = Stock.objects.filter(date__month=(request.session['game_round'] - 6))
        else:
            all_stocks = Stock.objects.filter(date__month=(request.session['game_round'] + 6))
        return render( request, 'game/round.html', {"game_round":game_round, "all_stocks":all_stocks, 'user':request.session.user}))


class Display_owned(View):
    def get(self, request):
        game_round = request.session['game_round']
        owned = Portfolio.objects.select_related('Stock_owned').filter(user=request.user)
        return render( request, 'game/round.html', {"game_round":game_round, "stock_owned":owned, 'user':request.session.user}))


class Buy_stock(View):
    def post(self, request):
        current = None
        return render( request, 'game/round.html', {"game_round":game_round, "stock_owned":owned, 'user':request.session.user}))
        #buy shares of a stock


class Sell_shares(View):
    def post(self, request):
        current = None
        return render( request, 'game/round.html', {"game_round":game_round, "stock_owned":owned, 'user':request.session.user}))
        #sell shares of a stock
