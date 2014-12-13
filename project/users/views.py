from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User

class Index(View):
    def get(self, request):
        return render( request, 'users/index.html' )

class Create(View):
    def get(self, request):
        return render( request, 'users/create.html' )

    def post(self, request):
        pass

class Login(View):
    def get(self, request):
        return render( request, 'users/login.html' )

    def post(self, request):
        pass

class Welcome(View):
    pass

class Logout(View):
    pass
        