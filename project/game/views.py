from django.views.generic import View
from django.shortcuts import render


class Round(View):
    def get(self, request):
        #how do we save game round info and score and pass it around?
        game_round = None
        if game_round == 12:
            return redirect('game/endgame.html')
        else:
            game_round ++ 1
            return render( request, 'game/round.html', {"game_round":game_round})

class Endgame(View):
    def get(self, request):
        #show final score, game history
        histor = None
        final = None
        return render( request, 'game/endgame.html', {"final":final, "history":history})
