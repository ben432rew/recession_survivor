from django import forms
from game.models import Stock, Whole_Game

# class StockForm(ModelForm):
#     class Meta:
#         model = Stock
#         fields = ('price', 'date', 'ticker')

class GameCreateForm( forms.ModelForm ):
	start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'special'}))

	class Meta:
		model = Whole_Game
		fields = ('game_type', 'start_date')