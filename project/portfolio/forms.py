from portfolio.models import *
from django.forms import ModelForm
from portfolio.models import Stocks_Tracked
from django import forms
from pprint import pprint as print

class DateInput( forms.DateInput ):
    input_type = 'date'

class portfolio_form( ModelForm ):
    class Meta:
        model = Portfolio
        fields = ('title', 'description')

class ModelChoiceField( forms.ModelChoiceField ):
    def label_from_instance( self, obj ):
        return str( obj['name'] )

class holding_form( ModelForm ):
    symbol = forms.fields.ChoiceField( Stocks_Tracked.objects.all().values_list('symbol', 'name')  )
    class Meta:
        model = Holding
        fields = ( 'symbol', 'price', 'shares', 'date' )
        widgets = {
            'date': DateInput(),
        }
