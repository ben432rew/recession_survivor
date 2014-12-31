import portfolio.models as models
from portfolio.forms import portfolio_form, holding_form
from django.utils.text import slugify
from django.contrib.auth.models import User
# from pprint import pprint as print

class Portfolio:
    current = None
    title = None
    description = None

    def __init__( self, arg1 ):
        arg1_type = type( arg1 )
        if isinstance( arg1, int ):
            self.set_current( models.Portfolio.objects.get( id=arg1 ) )

        elif isinstance( arg1, str ):
            print('string')
            self.set_current( models.Portfolio.objects.get( slug=arg1 ) )

    def set_current( self, portfolio ):
        self.current = portfolio
        self.title = portfolio.title
        self.description = portfolio.description
        self.stocks = models.Holding.objects.filter( portfolio = portfolio )

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
        print( dir( results))
        return results

    def remove_holding(self,user_id):
        pass
    