from portfolio.models import *
from django.forms import ModelForm
from django import forms
from pprint import pprint as print
from django.core.exceptions import ValidationError

def val_share(shares):
    if float(shares)<= 0 or shares == "" :
        raise ValidationError("Shares must be greater than zero ")

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
    shares = forms.IntegerField(validators=[val_share])
    symbol = forms.fields.ChoiceField( Stocks_Tracked.objects.all().values_list('symbol', 'name')  )
    class Meta:
        model = Holding
        fields = ( 'symbol', 'shares' )
        widgets = {
            'date': DateInput(),
        }
