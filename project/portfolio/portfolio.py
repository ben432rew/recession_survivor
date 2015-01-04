import portfolio.models as models
from portfolio.forms import portfolio_form, holding_form
from django.utils.text import slugify
from game.models import Whole_Game
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from pprint import pprint

# portfolio should have a "value"  of all holdings
# and it should take a "current_date" and reference the Stocks_history table for pirces
# there should like "__compute_value" function in the portfolio object 

# today = str( datetime.date.today() )

class Portfolio:
<<<<<<< HEAD
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
=======
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
            self.current_date =  datetime.strftime( datetime.today() ,"%Y-%m-%d")

        ## get portfolio based on ID or slug(title)
        id_or_slug_type = type( id_or_slug )

        if isinstance( id_or_slug, int ):
            portfolio = models.Portfolio.objects.get( id=id_or_slug )

        elif isinstance( id_or_slug, str ):
            portfolio = models.Portfolio.objects.get( slug=id_or_slug )

        for key, value in portfolio.__dict__.items():
            setattr( self, key, value )

>>>>>>> cb5a932292eba2ac2b2c44a19fdfa895383e2191
        self.current = portfolio

<<<<<<< HEAD
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
=======
        self.__load_stocks()

    def __load_stocks( self ):
        '''
        Load all the holdings of current portfolio, total them up, build stocks dict
        '''
        self.stocks = {} # clear old data
        holdings = models.Holding.objects.filter( portfolio=self.current )
>>>>>>> cb5a932292eba2ac2b2c44a19fdfa895383e2191

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
<<<<<<< HEAD
    def create( cls, form, user_id ):

        if form.is_valid():
            data = form.cleaned_data
            data[ 'user' ] = User.objects.get( id=user_id )
            data[ 'slug' ] = slugify( data[ 'title' ] )
            data = models.Portfolio.objects.create( **data )
            return data
        else:
            return False
=======
    def create( cls, data):

        '''
        Create new portfolio from create_form data and user_id argument
        '''
        
        data['slug'] = slugify( data[ 'title' ] )
        data = models.Portfolio.objects.create( **data )

        return data
>>>>>>> cb5a932292eba2ac2b2c44a19fdfa895383e2191

    # notice different naming
    create_holding = holding_form
    
<<<<<<< HEAD
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
=======
    def add_holding( self, data ):

        value = data['shares']*data['price']

        data['portfolio'] = self.current

        data = models.Holding.objects.create( **data )

        self.__load_stocks()

        return value

    def remove_holding( self, symbol, amount ):

        # checks to see if 
        if symbol not in self.stocks:
>>>>>>> cb5a932292eba2ac2b2c44a19fdfa895383e2191
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

    def change_date( self, date ):
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
        if date_in.strftime("%A") == "Sunday":
            date_in -= datetime.timedelta(days=2)
            return date_in
        elif date_in.strftime("%A") == "Saturday":
            date_in -= datetime.timedelta(days=1)
            return date_in
        else:
            return date_in

    def stock_date( self, symbol, date=False ):
        if not date:
            date = self.current_date
        print(date)
        results = models.Stock_history.objects.filter( symbol=symbol, date=date )
        while(len(results)==0):
            date -= timedelta(days=1)
            results = models.Stock_history.objects.filter( symbol=symbol, date=date )
        results = results[0]

        return results
