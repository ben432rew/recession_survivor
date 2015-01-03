import portfolio.models as models
from portfolio.forms import portfolio_form, holding_form
from django.utils.text import slugify
from game.models import Whole_Game
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

    def __init__( self, id_or_slug, date=False ):

        # set date for price eval
        if date:
            self.current_date = self.check_date( date )
        else:
            # as soon as check date works this should be set today.
            self.current_date = self.check_date( '2014-12-30' ) # datetime.strftime( datetime.today() ,"%Y-%m-%d")

        ## get portfolio based on ID or slug(title)
        id_or_slug_type = type( id_or_slug )

        if isinstance( id_or_slug, int ):
            portfolio = models.Portfolio.objects.get( id=id_or_slug )

        elif isinstance( id_or_slug, str ):
            portfolio = models.Portfolio.objects.get( slug=id_or_slug )

        for key, value in portfolio.__dict__.items():
            setattr( self, key, value )

        self.current = portfolio

        self.__load_stocks()

    def __load_stocks( self ):
        '''
        Load all the holdings of current portfolio, total them up, build stocks dict
        '''
        self.stocks = {} # clear old data
        holdings = models.Holding.objects.filter( portfolio=self.current )

        for hold in holdings:

            # dont let untracked holdings kill the script... should something deferent here
            try:
                stock_hist = models.Stock_history.objects.filter( symbol=hold.symbol )[0]
            except:
                continue

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
    def create( cls, data, user_id ):

        '''
        Create new portfolio from create_form data and user_id argument
        '''

        data['user'] = User.objects.get( id=user_id )
        data['slug'] = slugify( data[ 'title' ] )
        data = models.Portfolio.objects.create( **data )

        return data

    # notice different naming
    create_holding = holding_form
    
    def add_holding( self, data ):

        value = data['shares']*data['price']
        
        data['portfolio'] = self.current

        data = models.Holding.objects.create( **data )

        self.__load_stocks()

        return value

    def remove_holding( self, symbol, amount ):

        # checks to see if 
        if symbol not in self.stocks:
            return False

        amount = int( amount )

        # checks to make user has the shares
        if self.stocks[symbol]['shares'] < amount or amount == 0:
            return False

        # generate the 
        value = amount*self.stocks[symbol]['close']

        holdings = models.Holding.objects.filter( portfolio=self.current, symbol=symbol )

        # remove the holdings
        for hold in holdings:

            # kill the loop is all shares have been removed
            if amount == 0: 
                break

            # if the holding is smaller then they shares left to remove, delete it and move on
            if hold.shares <= amount:
                amount -= hold.shares
                hold.delete()

            # or if holding is smaller then amount, edit the hold and kill the loop 
            else:
                hold.shares -= amount
                hold.save()
                break

        self.__load_stocks() # update stock data

        # return value of effected holdings
        return value

    def chage_date( self, date ):
        '''
        Changes the date of the eval history date. This will update prices in self.stocks as well.
        This should also handle splits and set the correct shares
        ''' 
        self.current_date = self.check_date( date )
        self.__load_stocks()
        return date

    def check_date( self, date_in ):
        ''' issue #125 '''
        return date_in
        date_in = datetime.strptime( date_in,"%Y-%m-%d")
        if date_in.weekday(6):
            date_in -= datetime.timedelta(days=2)
            return date_in
        elif date_in.weekday(5):
            date_in -= datetime.timedelta(days=1)
            return date_in

    def stock_date( self, symbol, date=False ):
        if not date:
            date = self.current_date

        results = models.Stock_history.objects.get( symbol=symbol, date=date )

        return results