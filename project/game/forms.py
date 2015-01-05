from django import forms
from game.models import *
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from pprint import pprint as print
from django.core.exceptions import ValidationError
import datetime

def date_far_enough(data):
    cur_date = datetime.datetime.strptime( data['current_date'], "%Y-%m-%d" ).date() 
    total_round = data['total_rounds']
    game_type = data['game_type']

    num_days = _cal_num_days(game_type, total_round)
    check_date = datetime.datetime.now().date() - datetime.timedelta(days=num_days)

    if(check_date <= cur_date):
        raise forms.ValidationError('Date must be further in the past')

def _cal_num_days(game_type, total_round):
    if game_type == 'weekly':
        num_days = 7 * total_round
    elif game_type == 'monthly':
        num_days = 31 * total_round
    elif game_type == 'yearly':
        num_days = 365 * total_round
    return num_days


def val_round(val_round):
    if (val_round<=0):
        raise ValidationError("Round must be greater 0", code='invalid')

def val_bal(bal):
    if(bal<=0):
        raise ValidationError("Balance must be greater than 0",code='invalid')

def val_date(date):

    d = datetime.datetime.now()
    dated = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    if (dated >= d.date()):
        raise ValidationError("This date must be in the past", code='invalid')

class DateInput(forms.DateInput):
    input_type = 'date'

# RegexValidator
class GameCreateForm( ModelForm ):
    balance = forms.DecimalField(initial=10000)
    total_rounds = forms.IntegerField(initial=12)
    current_date = forms.CharField( widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Whole_Game
        fields = ( 'name', 'start_balance', 'total_rounds' , 'game_type', 'current_date' )
        widgets = {
            'current_date' : DateInput()
        }
        labels = {
            'current_date': _('Starting Day of Your Game (use format 9/20/2011)')
        }

    def clean(self):
        if (self.is_valid()==False):
            raise forms.ValidationError('Please enter all fields')

        data = self.cleaned_data
        val_round(data['total_rounds'])
        val_date(data['current_date'])
        val_bal(data['balance'])
        date_far_enough(data)

        return self.cleaned_data
        