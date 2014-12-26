from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View

# Create your views here.

class Index( View ):
    def get( self, request ):
        context_dict = {}
        if request.is_ajax():
            context_dict['base_template'] = "ui/ajax.html"
            
        return render( request, 'ui/index.html', context_dict)
