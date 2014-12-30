from django.shortcuts import render, redirect
from django.views.generic import View
from blog.models import Post
from blog.forms import PostForm
from django.contrib.auth.models import User
from django.utils.text import slugify

class IndexView(View):
    template = 'blog/index.html'

    def get( self, request ):

        return render( request, self.template , request.context_dict )

class Create(View):
    template = 'blog/create.html'

    def get(self,request):
        if request.user.is_anonymous():
            return redirect( '/' )

        request.context_dict['form'] = PostForm()

        return render( request, self.template, request.context_dict )
    
    def post(self,request):
        form = PostForm( request.POST )

        if form.is_valid():
            data = form.cleaned_data
            data['user_id'] = User.objects.get( id=request.user.id )
            data['slug'] = slugify( request.POST['title'] )
            data = Post.objects.create( **data )

            return redirect( 'post/{}'.format( data.slug ) )

        request.context_dict['form'] = form

        return render( request, self.template, request.context_dict )

class BlogDisplayView(View):
    template = 'blog/display.html'
    
    def get( self, request, slug ):
        request.context_dict['post'] = Post.objects.get( slug=slug )

        return render( request, self.template, request.context_dict )