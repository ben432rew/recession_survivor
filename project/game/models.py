from django.contrib.auth.models import User
from portfolio.models import Portfolio
from django.db import models

game_type_choices = (
    ('weekly', 'Weekly' ),
    ( 'monthly', 'Monthly' ),
    ( 'yearly', 'Yearly' ),
)

class Stock(models.Model):
    symbol = models.CharField(max_length=50)
    price = models.FloatField()
    date = models.DateField()
    volume = models.FloatField()

class Whole_Game(models.Model):
    game_type = models.CharField(max_length=30, choices=game_type_choices)
    name = models.CharField(max_length=30)
    start_balance = models.FloatField(default=10000)
    balance = models.FloatField(default=10000)
    final_score = models.FloatField(default=0)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, default=None)
    current_date = models.DateField()
    current_round = models.IntegerField(default=0)
    total_rounds = models.IntegerField(default=12)
    user = models.ForeignKey(User)
    portfolio_id = models.IntegerField()

    def change_date( self, date ):

        # up date the current portfolio date
        self.portfolio.change_date( self.current_date )

        # sync with portfolio date
        self.current_date = self.portfolio.current_date

        return date

class Transaction(models.Model):
    symbol = models.CharField(max_length=50)
    number_of_shares = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    account_change = models.FloatField()
    portfolio = models.ForeignKey(Portfolio)
