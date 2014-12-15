from django.contrib.auth.models import User
from django.db import models


class Portfolio(models.Model):
	final_score = models.FloatField(default=None)
	date_played = models.DateField(auto_now=True)
	user = models.ForeignKey(User)
	balance = models.FloatField()


class Transcation(models.Model):
	symbol = models.CharField(max_length=50)
	number_of_shares = models.IntegerField()
	date_created = models.DateField(auto_now_add=True)
	account_change = models.FloatField()
	portfolio = models.ForeignKey('Portfolio')


class Stock_owned(models.Model):
	symbol = models.CharField(max_length=50)
	amount = models.IntegerField()
	price_bought = models.FloatField()
	date_bought = models.DateField()
	name = models.CharField(max_length=50)
	portfolio = models.ForeignKey('Portfolio')


class Stock(models.Model):
	symbol = models.CharField(max_length=50)
	price = models.FloatField()
	date = models.DateField()
	name = models.CharField(max_length=50)
	volume = models.FloatField()


class snippet(models.Model):
	stock = models.ForeignKey('Stock')
	snippet = models.TextField()