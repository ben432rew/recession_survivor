from django.shortcuts import render,redirect
from portfolio.forms import Stock_list
from portfolio.models import Portfolio
from django.views.generic import View
from game.models import *


class Index(View):
    def get(self, request):
        if not request.user.is_authenticated():
            return redirect('/users/login/?error={}'.format("You must sign in first"))
        unfinished = Whole_Game.objects.filter(user=request.user, final_score=0)
        if len(unfinished) == 0:
            return render(request, 'game/index.html', {'user':request.user, 'unfinished':None , "form" : Stock_list()})
        else:
            return render(request, 'game/index.html', {'user':request.user, 'unfinished':unfinished[0]})


class Games_history(View):
    def get(self, request):
        if not request.user.is_authenticated():
            return render('/users/login/?error={}'.format("You must sign in first"))        
        whole_games = Whole_Game.objects.filter(user = request.user).order_by(date_played)
        return render(request, 'game/history.html', {'user':request.user, 'whole_games':whole_games})


class Round(View):
    #first time the round will be called by a GET, every time after will be a POST
    def get(self, request):
        #june 2009 and june 2008 exist in the db now, deleting june 2009 for easy querying
        extras = Stock.objects.filter(date__month=6, date__year=2009).delete()
        if not request.user.is_authenticated():
            return render('/users/login/?error={}'.format("You must sign in first"))        
        p = Whole_Game.objects.create(user=request.user, balance=10000)        
        request.session['game_round'] = 0
        request.session['balance'] = 10000        
        return render(request, 'game/round.html', {'user':request.user, 'balance':'$10,000.00'})

    def post(self, request):
        if request.session['game_round'] == 12:
            return redirect('game/endgame.html')
        else:
            request.session['game_round'] += 1
            return render( request, 'game/round.html', {'user':request.user, 'balance':request.session['balance']})


class Endgame(View):
    def get(self, request):
        #sell all stocks, calculate new balance, show game transactions
        balance = request.session['balance']
        owned = Whole_Game.objects.select_related('Portfolio').filter(user=request.user)
        for stock in owned:
            current_priced_stock = Stock.objects.get(symbol=symbol, date__month=(request.session['game_round'] + 6) % 12)
            balance += (current_priced_stock.price * stock.amount)
            current_priced_stock.delete()
        whole_game = Whole_Game.objects.filter(user=request.user).order_by('date')[0]
        whole_game.final_score = balance
        whole_game.save()
        trans = Transaction.objects.filter(whole_game=whole_game).order_by(date_created)
        return render( request, 'game/endgame.html', {"balance":balance, "history":trans})