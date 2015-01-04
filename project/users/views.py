from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import render, redirect
from portfolio.models import Portfolio
from django.views.generic import View
from game.models import Whole_Game


class Index(View):
    def get(self, request):
        if request.user.is_anonymous():
            request.context_dict[ 'create_form' ] = UserCreationForm()
            request.context_dict[ 'login_form' ] = AuthenticationForm()

            return render( request, 'users/index.html', request.context_dict )
        else:
            return redirect('/blog')


class Signup(View):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            a = User.objects.create_user( username=cd.get('username'), password=cd.get('password1'))
            return redirect('/?error={}'.format("signup a success! now please login") )
        else:
            request.context_dict[ 'create_form' ] = form
            request.context_dict[ 'login_form' ] = AuthenticationForm()

            return render( request, 'users/index.html', request.context_dict )


class Login(View):
    def post(self, request):

        # odd that None is needed...
        # http://stackoverflow.com/a/21504550/3140931
        form = AuthenticationForm( None,request.POST )

        if form.is_valid():
            login(request, form.get_user())
            
            return redirect('/blog')
        else:
            request.context_dict[ 'create_form' ] = UserCreationForm()
            request.context_dict[ 'login_form' ] = form

            return render( request, 'users/index.html', request.context_dict )

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect( '/')


class Profile(View):
    def get(self, request):
        if request.user.is_anonymous():
            return redirect( '/')
        else:
            request.context_dict['game'] = Whole_Game.objects.filter(final_score=0)
            request.context_dict['highscores'] = Whole_Game.objects.all().order_by('final_score')[:9]
            request.context_dict['form'] = PasswordChangeForm(request.user)
            return render( request, 'users/profile.html', request.context_dict)


class ChangePass(View):
    def post(self, request):
        user = authenticate(username=request.user.username, password=request.POST["old_password"])
        if request.POST['new_password1'] != request.POST['new_password2']:
            return redirect ('/users/profile/?error={}'.format("new passwords don't match"))
        if user is not None:
            user.set_password(request.POST['new_password1'])
            user.save()
            return redirect ('/users/profile')
        else:
            return redirect ('/users/profile/?error={}'.format("incorrect password"))
