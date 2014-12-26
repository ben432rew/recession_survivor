from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	slug = models.CharField(max_length=200)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
