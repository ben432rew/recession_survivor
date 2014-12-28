from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import render, redirect
from portfolio.models import Portfolio
from django.views.generic import View
from game.models import Whole_Game


class Index(View):
    def get(self, request):
        if request.user.is_anonymous():
            request.context_dict[ 'form' ] = UserCreationForm()
            return render( request, 'users/index.html', request.context_dict )
        else:
            return redirect('/users/welcome')


class Signup(View):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            a = User.objects.create_user( username=cd.get('username'), password=cd.get('password1'))
            return redirect('/?error={}'.format("signup a success! now please login") )
        else:
            return render(request, '/users/index.html', {'error':"Not a valid name or password", 'form':UserCreationForm(request.POST) } )


class Login(View):
    def post(self, request):
        username = request.POST["username_l"]
        password = request.POST["password_l"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/users/welcome')
        else:
            return render(request, 'users/index.html', {"error":"incorrect username/password combination"})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect( '/')


class Welcome(View):
    def get(self, request):
        if request.user.is_anonymous():
            return redirect( '/')
        else:
            request.context_dict['game'] = Whole_Game.objects.filter(final_score=0)
            request.context_dict['saved_game'] = True if len( request.context_dict['game'] ) > 0 else False
            request.context_dict['scores'] = Whole_Game.objects.all().order_by('final_score')[:9]
            request.context_dict['form'] = PasswordChangeForm(request.user)
            return render( request, 'users/welcome.html', request.context_dict)


class ChangePass(View):
    def post(self, request):
        user = authenticate(username=request.user.username, password=request.POST["old_password"])
        if request.POST['new_password1'] != request.POST['new_password2']:
            return redirect ('/users/welcome/?error={}'.format("new passwords don't match"))
        if user is not None:
            user.set_password(request.POST['new_password1'])
            user.save()
            return redirect ('/users/welcome')
        else:
            return redirect ('/users/welcome/?error={}'.format("incorrect password"))