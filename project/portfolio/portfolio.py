import portfolio.models as models
from portfolio.forms import portfolio_form, holding_form
from django.utils.text import slugify
from game.models import Whole_Game
from django.contrib.auth.models import User
import datetime
# from pprint import pprint as print

# portfolio should have a "value"  of all holdings
# and it should take a "current_date" and reference the Stocks_history table for pirces
# there should like "__compute_value" function in the portfolio object 



class Portfolio:
    current = None
    title = None
    description = None
    # all the holding price added up
    value = 0


    def __init__( self, arg1 ):
        arg1_type = type( arg1 )
        if isinstance( arg1, int ):
            self.set_current( models.Portfolio.objects.get( id=arg1 ) )

        elif isinstance( arg1, str ):
            port = models.Portfolio.objects.get( slug=arg1 )
            self.set_current( port )
            self.set_value_all_holding( port )

    def set_current( self, portfolio ):
        self.current = portfolio
        self.title = portfolio.title
        self.description = portfolio.description
        self.stocks = models.Holding.objects.filter( portfolio = portfolio )

    def set_value_all_holding(self,portfolio):
        stocks = self.stocks
        for stock in stocks:
            self.value += (stock.price * stock.shares)


    create_form = portfolio_form

    @classmethod
    def create( cls, form, user_id ):
        if form.is_valid():
            data = form.cleaned_data
            data[ 'user' ] = User.objects.get( id=user_id )
            data[ 'slug' ] = slugify( data[ 'title' ] )
            data = models.Portfolio.objects.create( **data )
            return data
        else:
            return False

    # notice different naming
    create_holding = holding_form
    
    def add_holding( self, form, user_id, request ):
        if form.is_valid():
            data = form.cleaned_data
            data[ 'portfolio' ] = self.current
            data[ 'shares' ] = request.POST['shares']
            data[ 'date' ] = datetime.datetime.strptime(request.POST['date'][0:10],"%Y-%m-%d")
            info = str.split(request.POST['stock'], '-')
            data[ 'symbol' ] = info[0]
            data[ 'price' ] = float(info[1])
            game =  Whole_Game.objects.get(id=request.session['game_id'])
            game.balance -= float(data['price']) * int(data['shares'])
            game.save()
            data = models.Holding.objects.create( **data )
            return data
        else:
            return False

    def by_user_id( self, user_id ):
        results =  models.Portfolio.objects.filter( user = User.objects.get( id=user_id ) )
        return results

    def remove_holding(self,request):
        data = request.POST
        holding = models.Holding.objects.get(id=data['stockid'])
        if holding.shares < int(data['shares']):
            return False
        else:
            holding.shares -= int(data['shares'])
            holding.save()
            game =  Whole_Game.objects.get(id=request.session['game_id'])
            print('before', game.balance)
            game.balance += float(data['price']) * int(data['shares'])
            print('after', game.balance)
            game.save()
            self.clear_zeros_shares()
            return True

    def clear_zeros_shares(self):
        models.Holding.objects.filter(shares=0).delete()