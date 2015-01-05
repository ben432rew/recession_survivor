from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from portfolio.portfolio import Portfolio
from portfolio.models import Stocks_Tracked
from datetime import datetime
from django.contrib.auth.decorators import login_required

## nothing about game belongs in this file
class Display_all( View ):
    def get( self, request ):
        if request.user.is_anonymous():
            return redirect('/')
        user_id = request.GET.get( 'user_id', request.user.id )
        request.context_dict[ 'portfolios' ] = Portfolio.by_user_id( user_id )
        
        return render( request, 'portfolio/display_all.html', request.context_dict )

class Create( View ):

    def get( self, request ):
        if request.user.is_anonymous():
            return redirect('/')
        request.context_dict[ 'form' ] = Portfolio.create_form()
        
        return render( request, 'portfolio/create.html', request.context_dict )

    def post( self, request ):
        form = Portfolio.create_form( request.POST )

        if form.is_valid():
            data = form.cleaned_data
            data['user'] = User.objects.get( id=request.user.id )
            results = Portfolio.create( data )
            
            return redirect( '/portfolio/{}/manage'.format( results.slug ) )

        request.context_dict[ 'form' ] = form
        
        return render( request, 'portfolio/create.html', request.context_dict )


class Manage( View ):
    def get( self, request, slug ):
        if request.user.is_anonymous():
            return redirect('/')
        date = request.POST.get( 'date' , '2014-12-30' ) # needs to be set to today if blank
        request.context_dict[ 'portfolio' ] = Portfolio( slug, date )

        return render( request, 'portfolio/manage.html', request.context_dict )

# needs to be converted to portfolio.py 
class Holding_add( View ):
    
    def get( self, request, slug ):
        if request.user.is_anonymous():
            return redirect('/')
        request.context_dict[ 'portfolio' ] = Portfolio( slug )
        request.context_dict[ 'form' ] = Portfolio.create_holding()
        
        return render( request, 'portfolio/holding_add.html', request.context_dict )

    def post( self, request, slug ):
        form = Portfolio.create_holding( request.POST )
        portfolio = Portfolio( slug, request.POST['date'] )

        if form.is_valid():
            form_data = form.cleaned_data
            form_data['date'] = request.POST['date']
            form_data['price'] = portfolio.stock_by_date( form_data['symbol'] ).close

            portfolio.add_holding( form_data )

            return redirect( '/portfolio/{}/manage'.format( slug ) )

        else:
            request.context_dict[ 'form' ] = form

            return render( request, 'portfolio/holding_add.html', request.context_dict )

class Holdin_remove( View ):
    def post( self, request, slug ):
        portfolio = Portfolio( slug )
        symbol = request.POST.get( 'symbol', None )
        amount = request.POST.get( 'amount', None )
        if portfolio.remove_holding( symbol, amount ):
            return redirect( '/portfolio/{}/manage'.format( slug ) )
        else:
            return redirect( '/portfolio/{}/manage'.format( slug ) )

# needs to be converted to portfolio.py and template created
class Edit( View ):
    
    def get( self, request, slug ):
        if request.user.is_anonymous():
            return redirect('/')
        request[ 'portfolio' ] = Portfolio.objects.get( slug=slug )
        request[ 'form' ] = portfolio_form( request[ 'portfolio' ] )
        
        return render( request, 'portfolio/edit.html', request.context_dict )

    def post( self, request, slug ):
        form = portfolio_form( request.POST )
        if form.is_valid():
            data = form.cleaned_data
            data[ 'slug' ] = slugify( request.POST[ 'title' ] )
            data = Post.objects.update( **data )

            return redirect( '/portfolio/{}'.format( data.slug ) )

        request.context_dict[ 'form' ] = portfolio_form( request.POST )
        request.context_dict[ 'error' ] = "Please review each field"
        
        return render( request, 'portfolio/create.html', request.context_dict )

class Tracked( View ):
    
    def get( self, request ):
        if request.user.is_anonymous():
            return redirect('/')
        request.context_dict['tracked'] = Stocks_Tracked.objects.all()
        
        return render( request, 'portfolio/tracked.html', request.context_dict )
