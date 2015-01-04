from django import forms
from game.models import *
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from pprint import pprint as print

class DateInput(forms.DateInput):
    input_type = 'date'

class GameCreateForm( ModelForm ):
    class Meta:
        model = Whole_Game
        fields = ( 'name', 'balance', 'total_rounds' , 'game_type', 'current_date' )
        widgets = {
            'current_date' : DateInput()
        }
        labels = {
            'current_date': _('Starting Day of Your Game (use format 9/20/2011)')
        }
