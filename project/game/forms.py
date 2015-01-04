from django import forms
from game.models import *
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from pprint import pprint as print
from django.core.exceptions import ValidationError
from datetime import datetime

def val_round(val_round):
    if (val_round<=0):
        raise ValidationError("Round must be greater 0")

def val_bal(bal):
    if(bal<=0):
        raise ValidationError("Balance must be greater than 0")

def val_date(date):
    d = datetime.now()
    dated = datetime.strptime(date, '%Y-%m-%d').date()
    if (dated == d.date()):
        raise ValidationError("This date must be in the past")

class DateInput(forms.DateInput):
    input_type = 'date'

class GameCreateForm( ModelForm ):
    balance = forms.DecimalField(validators=[val_bal])
    total_rounds = forms.IntegerField(validators=[val_round])
    current_date = forms.CharField(validators=[val_date],widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Whole_Game
        fields = ( 'name', 'balance', 'total_rounds' , 'game_type', 'current_date' )
        labels = {
            'current_date': _('Starting Day of Your Game (use format 9/20/2011)')
        }


