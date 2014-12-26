from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from portfolio.models import Portfolio
from django.views.generic import View
from django.shortcuts import render, redirect


class Index(View):
    def get(self, request):
        return render( request, 'users/index.html', {'form':UserCreationForm() } )


class Signup(View):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            a = User.objects.create_user( username=cd.get('username'), password=cd.get('password1'))
            return redirect('/users/login/?error={}'.format("signup a success! now please login") )
        else:
            return render(request, 'users/signup.html', {'error':"Not a valid name or password", 'form':UserCreationForm(request.POST) } )


class Login(View):
    def post(self, request):
        username = request.POST["username_l"]
        password = request.POST["password_l"]
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


class Welcome(View):
    def get(self, request):
        pass


class ChangePass(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class HighScores(View):
    def get(self, request):
        pass
