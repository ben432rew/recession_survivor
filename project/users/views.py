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
            return redirect('/users/login.html', {'error':"signup a success! now please login"})
        else:
            return render(request, 'users/create.html', {'error':"Not a valid name or password"})


class Login(View):
    def get(self, request):
        return render( request, 'users/login.html', {'form':UserForm()} )

    def post(self, request):
        form = UserForm(request.POST)        
        # username = request.POST["user_name"]
        # password = request.POST["password"]
        user = authenticate(**form.cleaned_data)
        if user is not None:
            login(request, user)
            return redirect('users/' + str(new_user.id))
        else:
            return render(request, 'users/login.html', {"error":"incorrect username/password combination"})


class Welcome(View):
    def get(self, request):
        unfinished = Portfolio.objects.filter(user=request.user, final_score=None)
        if len(unfinished) == 0:
            return render(request, 'users/welcome.html', {'user':request.user, 'unfinished':None})
        else:
            return render(request, 'users/welcome.html', {'user':request.user, 'unfinished':unfinished[0]})


class Games_history(View):
    def get(self, request):
        pass
        #show games history of user


class High_scores(View):
    def get(self, request):
        #need to change this to only get top ten
        scores = Portfolio.objects.all()
        return render(request, 'users/highscores.html', {'scores':scores})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect( 'users/index.html')