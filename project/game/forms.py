from django.forms import ModelForm
from game.models import Stock

class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = ('price', 'date', 'ticker')