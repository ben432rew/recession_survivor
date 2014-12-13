from django.db import models

# Create your models here.
class Stock(models.Model):
	price = models.IntegerField()
	date = models.DateField()
	# ticker = models.CharField(max_length=50)
