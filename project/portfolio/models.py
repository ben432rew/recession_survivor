from django.db import models
from django.contrib.auth.models import User

class Stock_history( models.Model ):
    symbol = models.CharField( max_length=50 )
    price = models.FloatField()
    date = models.DateField()

class Portfolio( models.Model ):
	title = models.CharField( max_length=200 )
	description = models.TextField()
	slug = models.CharField( max_length=200 )
	date_created = models.DateField( auto_now_add=True )
	user = models.ForeignKey( User )

class Holding( models.Model ):
	symbol = models.CharField( max_length=50 )
	date = models.DateField()
	price = models.FloatField()
	shares = models.FloatField()
	portfolio = models.ForeignKey( Portfolio )

class snippet( models.Model ):
    stock = models.ForeignKey( Stock_history )
    snippet = models.TextField()
    date = models.DateField()