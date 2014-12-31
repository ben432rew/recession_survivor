from django.shortcuts import render,redirect
from django.views.generic import View
# from portfolio.forms import Stock_list
from portfolio.models import *
from game.models import *
from game.forms import GameCreateForm
from django.template import RequestContext
import datetime

class Index( View ):
	form_class = GameCreateForm()

	def get( self, request):
		return render( request, 'game/index.html', { 'form' : self.form_class} )

class CreateView( View ):

	def post(self, request):
		print('went create')
		request.session['start_date'] = request.POST['start_date']
		request.session['game_type'] = request.POST['game_type']
		request.session['game_name'] = request.POST['game_name']
		user = User.objects.get(id=request.user.id)
		Portfolio.objects.create(user=user, title=request.session['game_name'], description=request.session['game_name'])
		portfolio = Portfolio.objects.last()
		request.session['portfolio_id'] = portfolio.id
		start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
		time = datetime.timedelta(days=28)
		end = start + time
		request.session['end_date'] = end
		Whole_Game.objects.create(user=user, game_type=request.session['game_type'], name=request.session['game_name'], start_date=request.session['start_date'], end_date=request.session['end_date'], current_date=request.session['start_date'], current_round=0, portfolio=portfolio)
		game = Whole_Game.objects.last()
		request.session['game_id'] = game.id
		if request.session['game_type'] == 'weekly':
			start = str( request.session['start_date'] )
			request.session['round'] = 0
			request.session['end_date'] = str( end ) 
			request.session['start_date_string'] = start[0:10]
			print(request.session['start_date_string'])
			request.session['add'] = True
			request.session.set_expiry(300)
		return redirect('/game/round/')

class RoundView( View ):
	template_name = 'game/round.html'

	def get(self, request):
		if request.session['round'] < 12 and request.session['add'] == True:
			request.session['round']+=1
			if request.session['game_type'] == 'weekly':
				print(request.session['round'])
				days = request.session['round']*7
				start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
				time = datetime.timedelta(days=days)
				end = start + time
				search_start = end - datetime.timedelta(days=7)
				stocks = Stock_history.objects.filter(date__range=[search_start, end])
				print(stocks)
				request.session['add'] = True
				return render(request, self.template_name, {'stocks':stocks})
			elif request.session['game_type'] == 'monthly':
				days = request.session['round']*31
				start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
				time = datetime.timedelta(days=days)
				end = start + time
				search_start = end - datetime.timedelta(days=31)
				request.session['search_start'] = search_start
				request.session['current_point'] = end
				stocks = Stock.objects.filter(date__range=[search_start, end])
				request.session['add'] = True
				return render(request, self.template_name, {'stocks':stocks})
			elif request.session['game_type'] == 'yearly':
				days = request.session['round']*365
				start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
				time = datetime.timedelta(days=days)
				end = start + time
				search_start = end - datetime.timedelta(days=365)
				request.session['search_start'] = search_start
				request.session['current_point'] = end
				stocks = Stock.objects.filter(date__range=[search_start, end])
				request.session['add'] = True
				return render(request, self.template_name, {'stocks':stocks})
			else:
				pass
		elif request.session['round'] < 12 and request.session['add'] == False:
			if request.session['game_type'] == 'weekly':
				days = request.session['round']*7
				start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
				time = datetime.timedelta(days=days)
				end = start + time
				search_start = end - datetime.timedelta(days=7)
				request.session['search_start'] = search_start
				request.session['current_point'] = end
				stocks = Stock.objects.filter(date__range=[search_start, end])
				request.session['add'] = True
				return render(request, self.template_name, {'stocks':stocks})
			elif request.session['game_type'] == 'monthly':
				days = request.session['round']*31
				start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
				time = datetime.timedelta(days=days)
				end = start + time
				search_start = end - datetime.timedelta(days=31)
				request.session['search_start'] = search_start
				request.session['current_point'] = end
				stocks = Stock.objects.filter(date__range=[search_start, end])
				request.session['add'] = True
				return render(request, self.template_name, {'stocks':stocks})
			elif request.session['game_type'] == 'yearly':
				days = request.session['round']*365
				start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
				time = datetime.timedelta(days=days)
				end = start + time
				search_start = end - datetime.timedelta(days=365)
				request.session['search_start'] = search_start
				request.session['current_point'] = end
				stocks = Stock.objects.filter(date__range=[search_start, end])
				request.session['add'] = True
				return render(request, self.template_name, {'stocks':stocks})
			else:
				pass
		else:
			return render(request, 'results.html')

class FindView( View ):
	template_name = 'game/find.html'

	def get(self, request):
		pass

class StatsView( View ):
	template_name = 'game/stats.html'

	def get(self, request):
		if request.session['game_type'] == 'weekly':
				print(request.session['round'])
				days = request.session['round']*7
				start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
				time = datetime.timedelta(days=days)
				end = start + time
				search_start = end - datetime.timedelta(days=7)
				stocks = Stock_history.objects.filter(date__range=[search_start, end])
				print(stocks)
				return render(request, self.template_name, {'stocks':stocks})
		elif request.session['game_type'] == 'monthly':
			days = request.session['round']*31
			start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
			time = datetime.timedelta(days=days)
			end = start + time
			search_start = end - datetime.timedelta(days=31)
			request.session['search_start'] = search_start
			request.session['current_point'] = end
			stocks = Stock.objects.filter(date__range=[search_start, end])
			return render(request, self.template_name, {'stocks':stocks})
		elif request.session['game_type'] == 'yearly':
			days = request.session['round']*365
			start = datetime.datetime.strptime(request.session['start_date'],"%Y-%m-%d")
			time = datetime.timedelta(days=days)
			end = start + time
			search_start = end - datetime.timedelta(days=365)
			request.session['search_start'] = search_start
			request.session['current_point'] = end
			stocks = Stock.objects.filter(date__range=[search_start, end])
			return render(request, self.template_name, {'stocks':stocks})
		else:
			pass

class PortfolioView( View ):
	template_name = 'game/portfolio.html'

	def get(self, request):
		pass