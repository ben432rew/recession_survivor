import portfolio.models as models
from portfolio.forms import portfolio_form, holding_form
from django.utils.text import slugify
from django.contrib.auth.models import User
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
            print('string')
            port = models.Portfolio.objects.get( slug=arg1 )
            self.set_current( port )
            self.set_value_all_holding( port )
            print(self.value)

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
        print

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
    
    def add_holding( self, form, user_id ):
        if form.is_valid():
            data = form.cleaned_data
            data[ 'portfolio' ] = self.current
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
        if holding.shares < int(data['sellstock']):
            return False
        else:
            print(holding.id)
            print(holding.shares)
            holding.shares -= int(data['sellstock'])
            print(holding.shares)
            holding.save()
            return True 
    