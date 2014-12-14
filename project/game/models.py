from django.db import models


class Stock(models.Model):
	price = models.IntegerField()
	date = models.DateField()
	ticker = models.CharField(max_length=50)
