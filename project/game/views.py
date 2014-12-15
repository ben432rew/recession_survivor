from django.views.generic import View
from django.shortcuts import render
from portfolio.models import Stock


class Round(View):
    #first time the round will be called by a GET, every time after will be a POST
    def get(self, request):
        #june 2009 and june 2008 exist in the db now, deleting june 2009 for easy querying
        extras = Stock.objects.filter(date__month=6, date__year=2009).delete()
        request.session['game_round'] = 0
        return render(request, 'game/round.html', {'user':request.user})

    def post(self, request):
        if request.session['game_round'] == 12:
            return redirect('game/endgame.html')
        else:
            request.session['game_round'] += 0
            return render( request, 'game/round.html', {'user':request.user})


class Endgame(View):
    def get(self, request):
        #show final score, game history
        histor = None
        final = None
        return render( request, 'game/endgame.html', {"final":final, "history":history})
