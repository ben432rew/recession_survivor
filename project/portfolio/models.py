from django.db import models

# Create your models here.
class Portfolio(models.Model):
	final_score = models.FloatField()
	date_played = models.DateTimeField(auto_now=True)
	user = models.ForeignKey('h_trader.User')
	balance = models.FloatField()

class Transcation(models.Model):
	symbol = models.CharField(max_lenght=50)
	number_of_shares = models.IntegerField()
	date_created = models.DateTimeField(auto_now_add=True)
	account_change = models.FloatField()
	portfolio = models.ForeignKey('h_trader.Portfolio')

class Stock_owned(models.Model):
	symbol = models.CharField(max_lenght=50)
	amount = models.IntegerField()
	price_bought = models.FloatField()
	date_bought = models.DateField()
	name = models.CharField(max_lenght=50)
	portfolio = models.ForeignKey('h_trader.Portfolio')

class Stock(models.Model):
	symbol = models.CharField(max_lenght=50)
	price = models.FloatField()
	date = models.DateField()
	name = models.CharField(max_lenght=50)
	volume = models.FloatField()

class snippet(models.Model):
	stock = models.ForeignKey('h_trader.Stock')
	snippet = models.TextField()