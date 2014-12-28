from django import template
from blog.models import Post
register = template.Library()

@register.inclusion_tag("blog/_posts.html")
def list_posts():
	posts = Post.objects.all()
	return { 'posts' : posts }
