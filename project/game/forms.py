from django import forms
from game.models import *
from django.forms import ModelForm
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
