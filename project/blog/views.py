from django.shortcuts import render, redirect
from django.views.generic import View
from blog.models import Post
from blog.forms import PostForm
# from blog.forms import PostForm

# Create your views here.
def slug_title(string):
    slug = ""
    for letter in string:
        if letter.isdigit() or letter.isalpha():
            slug += letter
        if(letter.isspace()):
            slug += "-"
    return slug

class IndexView(View):
    template = 'blog/index.html'

    def get( self, request ):
        # posts = Post.objects.all()
        context_dict = {}
        if request.is_ajax():
            context_dict['base_template'] = "ui/ajax.html"

        return render( request, self.template , context_dict )

class BlogPostView(View):
    template = 'blog/blog.html'

    def get(self,request):
        context_dict = {}
        if request.is_ajax():
            context_dict['base_template'] = "ui/ajax.html"
        context_dict['form'] = PostForm()
        return render( request, self.template, context_dict )
    
    def post(self,request):
        data = PostForm(request.POST)
        post_obj = data.save()
        post_obj.slug = slug_title(request.POST['title'])
        post_obj.save()
        return redirect('post/{}'.format(post_obj.slug))

class BlogDisplayView(View):
    template = 'blog/display.html'
    
    def get( self, request, slug ):
        context_dict = {}
        if request.is_ajax():
            context_dict['base_template'] = "ui/ajax.html"

        context_dict['post'] = Post.objects.get(slug=slug)
        return render( request, self.template, context_dict )