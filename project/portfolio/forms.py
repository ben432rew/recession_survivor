from portfolio.models import *
from django.forms import ModelForm
from django import forms
from pprint import pprint as print

class DateInput(forms.DateInput):
    input_type = 'date'

class portfolio_form( ModelForm ):
	class Meta:
		model = Portfolio
		fields = ('title', 'description')

class holding_form( ModelForm ):
	class Meta:
		model = Holding
		fields = ( 'symbol', 'price', 'shares', 'date' )
		widgets = {
            'date': DateInput()
        }


# class Portfolio(ModelForm):
# 	# how do i get the current user id to get all their portfolios
#     class Meta:
#         model = Portfolio
#         # fields =  forms.ModelChoiceField(queryset=port_arr)

# class Stock_owned(ModelForm):
# 	# need to know whats the users own stock to create a choicefield
# 	class Meta:
# 		model = Stock_owned

# class ModelChoiceField(forms.ModelChoiceField):
#     def label_from_instance(self, obj):
#         return str(obj.ticker)

# class Stock_list(forms.Form):		
# 		fields = ModelChoiceField(queryset=Stock.objects.all().distinct(),to_field_name="ticker")
# 	