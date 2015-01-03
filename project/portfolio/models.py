from django.db import models
from django.contrib.auth.models import User

class Stock_history( models.Model ):
    symbol = models.CharField( max_length=50 )
    date = models.DateField()
    open_price = models.FloatField() ## open is reserved word.
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.FloatField()
    dividend = models.FloatField() ## Ex-Dividend
    split_ratio = models.FloatField( null=True )

class Stocks_Tracked( models.Model ):
    symbol = models.CharField( max_length=50, unique=True )
    name = models.CharField( max_length=100 )
    from_date = models.DateField()
    to_date = models.DateField()

class Portfolio( models.Model ):
    title = models.CharField( max_length=200, unique=True  )
    description = models.TextField( null=True )
    slug = models.CharField( max_length=200 )
    date_created = models.DateField( auto_now_add=True )
    user = models.ForeignKey( User )

class Holding( models.Model ):
    symbol = models.CharField( max_length=50 )
    date = models.DateField()
    price = models.FloatField()
    shares = models.IntegerField()
    portfolio = models.ForeignKey( Portfolio )

class Snippet( models.Model ):
    stock = models.ForeignKey( Stock_history )
    snippet = models.TextField()
    date = models.DateField()