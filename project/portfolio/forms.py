from portfolio.models import *
from django.forms import ModelForm
from game.models import Stock
from django import forms


class Portfolio(ModelForm):
	# how do i get the current user id to get all their portfolios
    class Meta:
        model = Portfolio
        # fields =  forms.ModelChoiceField(queryset=port_arr)

class Stock_owned(ModelForm):
	# need to know whats the users own stock to create a choicefield
	class Meta:
		model = Stock_owned

class Stock(ModelForm):
	stock_arr = Stock.objects.all()
	class Meta:
		field = forms.ModelChoiceField(queryset=Stock.objects.all(), to_field_name="ticker")
	