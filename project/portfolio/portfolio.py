import portfolio.models as models
from portfolio.forms import portfolio_form, holding_form
from django.utils.text import slugify
from django.contrib.auth.models import User
from datetime import datetime
from pprint import pprint

# portfolio should have a "value"  of all holdings
# and it should take a "current_date" and reference the Stocks_history table for pirces
# there should like "__compute_value" function in the portfolio object 

# today = str( datetime.date.today() )

class Portfolio:
    current = None # current portfolio model
    title = None # current portfolio title
    description = None # current portfolio title
    value = 0 # current portfolio title at current date
    stocks = {} # list of stocks, totaled
    holdings = [] # list of holdings, model objects
    slug = ''

    def __init__( self, arg1, arg2=False ):

        ## set date for price eval
        if arg2:
            self.current_date = arg2
        else:
            self.current_date = '2014-12-30' # datetime.strftime( datetime.today() ,"%Y-%m-%d")

        ## get portfolio based on ID or slug(title)
        arg1_type = type( arg1 )
        if isinstance( arg1, int ):
            self.set_current( models.Portfolio.objects.get( id=arg1 ) )

        elif isinstance( arg1, str ):
            self.set_current( models.Portfolio.objects.get( slug=arg1 ) )
            # self.set_value_all_holding( port )

    def set_current( self, portfolio ):
        self.current = portfolio
        self.title = portfolio.title
        self.description = portfolio.description
        self.slug = portfolio.slug
        self.__load_stocks()

    def __load_stocks( self ):
        '''
        Load all the holdings of current portfolio, total them up, build stocks dict
        '''
        self.stocks = {} # clear old data
        holdings = models.Holding.objects.filter( portfolio=self.current )

        for hold in holdings:
            stock_hist = models.Stock_history.objects.filter( symbol=hold.symbol, date=self.current_date )[0]
            holding_value = hold.shares*stock_hist.close
            self.value += holding_value

            if hold.symbol in self.stocks:
                self.stocks[ hold.symbol ]['shares'] += hold.shares
                self.stocks[ hold.symbol ]['current_value'] += holding_value
            else:
                stock_data = models.Stocks_Tracked.objects.get( symbol=hold.symbol )

                self.stocks[ hold.symbol ] = stock_hist.__dict__
                self.stocks[ hold.symbol ]['name'] = stock_data.name
                self.stocks[ hold.symbol ]['shares'] = hold.shares
                self.stocks[ hold.symbol ]['current_value'] = holding_value

    @classmethod
    def by_user_id( cls, user_id ):
        '''
        return all portfolios for passed user_id
        '''

        results =  models.Portfolio.objects.filter( user=User.objects.get( id=user_id ) )
        return results

    create_form = portfolio_form

    @classmethod
    def create( cls, form, user_id ):
        '''
        Create new portfolio from create_form date and user_id argument
        '''

        if form.is_valid():
            data = form.cleaned_data
            data['user'] = User.objects.get( id=user_id )
            data['slug'] = slugify( data[ 'title' ] )
            data = models.Portfolio.objects.create( **data )

            return data
        else:
            return False

    # notice different naming
    create_holding = holding_form
    
    def add_holding( self, form, user_id ):
        if form.is_valid():
            data = form.cleaned_data
            data['portfolio'] = self.current
            data = models.Holding.objects.create( **data )
            return data
        else:
            return False

    def remove_holding( self, symbol, amount ):

        if symbol not in self.stocks:
            return False

        amount = int( amount )
        # print( 'amount', amount, 'has', self.stocks[symbol]['shares'] )
        if self.stocks[symbol]['shares'] < amount:
            return False

        value = amount*self.stocks[symbol]['close']

        holdings = models.Holding.objects.filter( portfolio=self.current, symbol=symbol )

        for hold in holdings:
            print( 'amount', amount, 'has', hold.shares )
            if amount == 0: 
                break

            if hold.shares <= amount:
                hold.delete()
            else:
                hold.shares -= amount
                hold.save()

        self.__load_stocks() # update stock data
        print( value)
        return value

    def check_date( self, date_in ):
        ''' issue #125 '''
        return date_in
 