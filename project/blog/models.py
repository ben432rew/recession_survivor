from django.db import models
from django.contrib.auth.models import User

category_choices = (
	( 'news', 'news' ),
	( 'help', 'help'),
	( 'user', 'user'),
)

# Create your models here.
class Post( models.Model ):
	title = models.CharField( max_length=200, unique=True)
	content = models.TextField()
	slug = models.CharField( max_length=200 )
	category = models.CharField( max_length=200, choices=category_choices )
	created_at = models.DateField( auto_now_add=True )
	updated_at = models.DateField( auto_now=True )
	user_id = models.ForeignKey( User )
