from django.shortcuts import render,redirect
from django.views.generic import View
from django.utils.text import slugify
from portfolio.models import *
from game.models import *
from game.forms import GameCreateForm
import datetime


def incrementer(time_span):
	if time_span == "weekly":
		return 7
	elif time_span == "monthly":
		return 30
	else:
		return 365

class CreateGame( View ):
	def get( self, request):
		request.context_dict['form'] = GameCreateForm()
		return render( request, 'game/index.html', request.context_dict )

	def post(self, request):
		form = GameCreateForm(request.POST)
		user = User.objects.get(id=request.user.id)
		if port == 'new_portfolio':
			Portfolio.objects.create(user=user, title=request.session['game_name'], description=request.session['game_name'], slug=slugify(request.POST['game_name']))
			portfolio = Portfolio.objects.last()
			request.session['portfolio_id'] = portfolio.id
			request.session['slug'] = portfolio.slug
		start = datetime.datetime.strptime(request.POST['start_date'],"%Y-%m-%d")
		game = Whole_Game.objects.create(user=user, balance=request.POST['initial_balance'], game_type=request.session['game_type'], name=request.session['game_name'], end_date=None, current_date=request.POST['start_date'], current_round=0, total_rounds=request.session['total_rounds'], portfolio=portfolio)
		request.session['game_id'] = game.id
		if request.session['game_type'] == 'weekly':
			start = str( request.POST['start_date'] )
			request.session['round'] = 0
			request.session['add'] = True
#how do we redirect and let the round know which game we're sending? whatever we do will also be needed for the Resume button on the unfinished games page
		return redirect('/game/round/')


class RoundView( View ):
	template_name = 'game/round.html'
# the round is incremented by 1 every round, but the date could be incremented by 7 days, 30 days, or 365 days
# which actually doesn't work because it doesn't account for leap years, months not 30 days long and most importantly, THE USER CAN ONLY ACTUALLY PLAY ON WEEKDAYS NOT WEEKENDS OR HOLIDAYS
# get should be used at the beginning of the first round.  Here the request.session variables should be set
	def get(self, request):
		request.session.set_expiry(300)
		if request.session['round'] < int(request.session["total_rounds"]) and request.session['add'] == True:
			request.session['round']+=1
			increment = incrementer(request.session['game_type'])
			days = request.session['round']*increment
			start = datetime.datetime.strptime(request.session['current_date'],"%Y-%m-%d")
			time = datetime.timedelta(days=increment)
			end = start + time
			search_start = end - datetime.timedelta(days=increment)
			request.session['search_start'] = str( search_start )
			request.session['current_date'] = str( end )
			stocks = Stock_history.objects.filter(date__range=[search_start, end])
			request.session['add'] = True
			game = Whole_Game.objects.get(id=request.session['game_id'])
			return render(request, self.template_name, {'stocks':stocks, 'game':game})
		elif request.session['round'] < int(request.session["total_rounds"]) and request.session['add'] == False:
			increment = incrementer(request.session['game_type'])
			days = request.session['round']*increment
			start = datetime.datetime.strptime(request.session['current_date'],"%Y-%m-%d")
			time = datetime.timedelta(days=days)
			end = start + time
			search_start = end - datetime.timedelta(days=increment)
			request.session['search_start'] = search_start
			request.session['current_date'] = end
			stocks = Stock.objects.filter(date__range=[search_start, end])
			request.session['add'] = True
			game = Whole_Game.objects.get(id=request.session['game_id'])
			return render(request, self.template_name, {'stocks':stocks, 'game':game})
		else:
			return render(request, 'results.html')
#everything else in the round should happen in a post
	def post(self, request):
		pass


class UnfinishedGames( View ):
	template_name = 'game/find.html'

	def get(self, request):
		request.context_dict['games'] = Whole_Game.objects.filter(user=request.user, end_date=None)
		return render(request, self.template_name, request.context_dict)


class StatsView( View ):
	template_name = 'game/stats.html'

	def get(self, request):
		if request.session['game_type'] == 'weekly':
				days = request.session['round']*7
				start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
				time = datetime.timedelta(days=days)
				end = start + time
				search_start = end - datetime.timedelta(days=7)
				stocks = Stock_history.objects.filter(date__range=[search_start, end])
				game = Whole_Game.objects.get(id=request.session['game_id'])
				return render(request, self.template_name, {'stocks':stocks, 'game':game})
		elif request.session['game_type'] == 'monthly':
			days = request.session['round']*31
			start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
			time = datetime.timedelta(days=days)
			end = start + time
			search_start = end - datetime.timedelta(days=31)
			request.session['search_start'] = search_start
			request.session['current_date'] = end
			stocks = Stock.objects.filter(date__range=[search_start, end])
			return render(request, self.template_name, {'stocks':stocks})
		elif request.session['game_type'] == 'yearly':
			days = request.session['round']*365
			start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
			time = datetime.timedelta(days=days)
			end = start + time
			search_start = end - datetime.timedelta(days=365)
			request.session['search_start'] = search_start
			request.session['current_date'] = end
			stocks = Stock.objects.filter(date__range=[search_start, end])
			return render(request, self.template_name, {'stocks':stocks})
		else:
			pass


class PortfolioView( View ):
	template_name = 'game/portfolio.html'

	def get(self, request):
		portfolio = Portfolio.objects.get(id=request.session['portfolio_id'])
		holdings = Holding.objects.filter(portfolio=portfolio)
		if holdings:
		# 	start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
		# 	current = datetime.datetime.strptime(request.session['current_date'],"%Y-%m-%d")
			stocks = Stock_history.objects.filter(date__range=[request.session['start_date_string'], request.session['end_date_string']])
			return render(request, self.template_name, {'holdings':holdings, 'stocks':stocks})
		else:
			start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
			current = datetime.datetime.strptime(request.session['current_date'][0:10],"%Y-%m-%d")
			stocks = Stock_history.objects.filter(date__range=[start, current])
			return render(request, self.template_name, {stocks:'stocks'})


class BuyView( View ):
	template_name = 'game/buy.html'

	def get(self, request):
		current = datetime.datetime.strptime(request.session['current_date'][0:10],"%Y-%m-%d")
		stocks = Stock_history.objects.filter(date=current)
		game = Whole_Game.objects.get(id=request.session['game_id'])
		portfolio = Portfolio.objects.get(id=request.session['portfolio_id'])
		return render(request, self.template_name, {'stocks':stocks, 'game':game, 'portfolio':portfolio})

#is this the view to sell shares from the portfolio?
class CheckoutView( View ):

	def post(self, request):
		post = str.split(request.POST['symbol'], '/')
		symbol = post[0]
		price = int(post[1])
		quantity = int(request.POST['quantity'])
		deduction = price * quantity
		current = datetime.datetime.strptime(request.session['current_date'][0:10],"%Y-%m-%d")
		portfolio = Portfolio.objects.get(id=request.session['portfolio_id'])
		Holding.objects.create(symbol=symbol, date=current, price=price, shares=quantity, portfolio=portfolio)
		game = Whole_Game.objects.get(id=request.session['game_id'])
		game.balance -= deduction
		game.save()
		return redirect('/game/round/portfolio/')

