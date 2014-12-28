from django.contrib.auth.models import User
from portfolio.models import Portfolio
from django.db import models

class Whole_Game(models.Model):
    final_score = models.FloatField(default=0)
    date_played = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    balance = models.FloatField()
    portfolio = models.ForeignKey(Portfolio)


class Transaction(models.Model):
    symbol = models.CharField(max_length=50)
    number_of_shares = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    account_change = models.FloatField()
