from portfolio.models import *
from django.forms import ModelForm
from game.models import Stock
from django import forms


# class Portfolio(ModelForm):
# 	# how do i get the current user id to get all their portfolios
#     class Meta:
#         model = Portfolio
#         # fields =  forms.ModelChoiceField(queryset=port_arr)

# class Stock_owned(ModelForm):
# 	# need to know whats the users own stock to create a choicefield
# 	class Meta:
# 		model = Stock_owned

class ModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return str(obj.ticker)

class Stock_list(forms.Form):
	
		# items = []
		# a = Stock.objects.all()
		# for x in a:
		# 	items.append(x)
		
		fields = ModelChoiceField(queryset=Stock.objects.all().distinct(),to_field_name="ticker")


	# class Meta:
		# model = Stock
		# print(Stock.objects.all())
		# to_field_name="ticker"
		# print( (Stock.objects.all()[0]).ticker )
		# , to_field_name="ticker"

		# stock_fields = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             # choices=a)
	