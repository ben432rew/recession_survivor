import portfolio.models as models
from portfolio.forms import portfolio_form, holding_form
from django.utils.text import slugify
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
    current_date = ""


    def __init__( self, arg1 , date):
        arg1_type = type( arg1 )
        if isinstance( arg1, int ):
            port = models.Portfolio.objects.get( id=arg1 )
            self.set_current( port )
            self.set_value_all_holding( port , date)

        elif isinstance( arg1, str ):
            port = models.Portfolio.objects.get( slug=arg1 )
            self.set_current( port )
            self.set_value_all_holding( port , date)

    def set_current( self, portfolio ):
        self.current = portfolio
        self.title = portfolio.title
        self.description = portfolio.description
        self.stocks = models.Holding.objects.filter( portfolio = portfolio )

    def set_value_all_holding(self,portfolio, date):
        stocks = self.stocks
        for stock in stocks:
            self.value += (self.get_price_at_date(date,stock.symbol) * stock.shares)

    def get_price_at_date(self , date_string, stock_symbol):
        # "2014-12-30" = date_string
        b = datetime.datetime.strptime( date_string , "%Y-%m-%d")
        current_date = b.date()
        stock_found = Stock_history.objects.filter( date=current_date , symbol=stock_symbol)
        return stock_found[0].close


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
            holding.shares -= int(data['sellstock'])
            holding.save()
            self.clear_zeros_shares()
            return True

    def clear_zeros_shares(self):
        models.Holding.objects.filter(shares=0).delete()