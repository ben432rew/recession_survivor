from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from portfolio.models import Portfolio
from django.views.generic import View
from django.shortcuts import render, redirect
from users.forms import UserForm


class Index(View):
    def get(self, request):
        return render( request, 'users/index.html' )


class Create(View):
    def get(self, request):
        return render( request, 'users/create.html', {'form':UserForm()} )

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            return redirect('/users/login/?error={}'.format("signup a success! now please login") )
        else:
            return render(request, 'users/create.html', {'error':"Not a valid name or password", 'form':UserForm(request.POST) } )


class Login(View):
    def get(self, request):
        error = request.GET.get( 'error', None )
        return render( request, 'users/login.html', {'form':UserForm(), 'error': error } )

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/game/')
        else:
            return render(request, 'users/login.html', {"error":"incorrect username/password combination"})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect( 'users/index.html')