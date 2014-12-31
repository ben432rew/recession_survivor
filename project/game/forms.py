from django import forms
from game.models import *
from django.forms import ModelForm
from pprint import pprint as print

class DateInput(forms.DateInput):
    input_type = 'date'

class GameCreateForm( ModelForm ):
	start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'special'}))

	class Meta:
		model = Whole_Game
		fields = ('game_type', 'start_date')
		widgets = {
			'start_date' : DateInput()
		}

