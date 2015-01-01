from django.contrib.auth.models import User
from portfolio.models import Portfolio
from django.db import models


class Stock(models.Model):
    symbol = models.CharField(max_length=50)
    price = models.FloatField()
    date = models.DateField()
    volume = models.FloatField()

class Whole_Game(models.Model):
    game_type = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    initial_balance = models.FloatField(default=10000)
    balance = models.FloatField(default=10000)
    final_score = models.FloatField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    current_date = models.DateField()
    current_round = models.IntegerField(default=0) 
    user = models.ForeignKey(User)
    portfolio = models.ForeignKey(Portfolio)


class Transaction(models.Model):
    symbol = models.CharField(max_length=50)
    number_of_shares = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    account_change = models.FloatField()
    portfolio = models.ForeignKey(Portfolio)
