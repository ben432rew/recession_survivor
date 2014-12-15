from django.views.generic import View
from django.shortcuts import render


class Round(View):
    def get(self, request):
        if 'game_round' in request.session.keys():
            if request.session['game_round'] == 12:
                return redirect('game/endgame.html')
            else:
                request.session['game_round'] += 1
                return render( request, 'game/round.html')
        else:
            request.session['game_round'] = 1
            return redirect('game/round.html')


class Endgame(View):
    def get(self, request):
        #show final score, game history
        histor = None
        final = None
        return render( request, 'game/endgame.html', {"final":final, "history":history})
