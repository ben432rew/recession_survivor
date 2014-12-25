from game.models import Whole_Game
from django.db import models


class Portfolio(models.Model):
	symbol = models.CharField(max_length=50)
	amount = models.IntegerField()
	price_bought = models.FloatField()
	date_bought = models.DateField()
	game = models.ForeignKey(Whole_Game)
