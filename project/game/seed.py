import requests
from game.models import Stock

tickers = ['GOOGL', 'MSFT', 'FB', 'YHOO', 'ORCL', 'IBM', 'AAPL', 'BBY', 'HPQ', 'AMZN', 'GE', 'XOM', 'CVX',
 'C', 'ED', 'CL', 'WSM', 'PG', 'K', 'HSY', 'DIS', 'COH', 'ALL', 'GIS', 'KWR', 'CAG', 'KO', 'PEP', 'M', 'WHR',
  'MKC', 'NKE', 'SJM', 'WFM', 'AEO', 'RL', 'HD', 'GPS', 'UA', 'CSCO', 'BBBY', 'GM', 'F', 'BAC', 'WMT', 'COST', 'JNJ', 'MET', 'VZ', 'T']

def seed():
	for ticker in tickers:
		r = requests.get("https://www.quandl.com/api/v1/datasets/WIKI/"+ ticker +".json?auth_token=M-1QA4sjxLA99bD7QjbN&trim_start=2008-06-01&trim_end=2009-06-01&column=4&collapse=monthly")
		mydata = r.json()
		ticker = mydata['code']
		print(ticker)
		for entry in mydata['data']:
			date = entry[0]
			price = entry[1]
			print(price, date)
			Stock.objects.create(price=price, date=date, symbol=ticker)

seed()