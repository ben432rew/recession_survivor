from django.shortcuts import render
from django.views.generic import View


class Index(View):
    def get( self, request ):
        return render( request, 'game/index.html' )

class Welcome(View):
    def get(self, request):
        pass
        #tell view if user has any unfinished games

class Start(View):
    def get(self, request):
        pass

class Round(View):
    def get(self, request):
        pass  

    def post(self, request):
        pass

class Endgame(View):
    def get(self, request):
        pass

