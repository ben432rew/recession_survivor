import requests
from portfolio.models import Stock_history, Stocks_Tracked
from pprint import pprint

symbols = [ 'KWR','GOOG', 'MSFT', 'FB', 'YHOO', 'ORCL', 'IBM', 'AAPL', 'BBY',
    'AMZN', 'GE', 'XOM', 'CVX', 'C', 'ED', 'CL', 'WSM', 'PG', 'K', 'HSY', 'DIS',
    'COH', 'ALL', 'GIS', 'CAG', 'KO', 'PEP', 'M', 'WHR', 'MKC', 'NKE', 'KWR',
    'SJM', 'WFM', 'AEO', 'RL', 'HD', 'GPS', 'UA', 'CSCO', 'BBBY', 'GM', 'F', 
    'BAC', 'WMT', 'COST', 'JNJ', 'MET', 'VZ', 'T' ]

# {"error":"Requested entity does not exist."} -- not tracked

def seed():
    for symbol in symbols:
        response = requests.get("https://www.quandl.com/api/v1/datasets/WIKI/"+ symbol +".json?auth_token=M-1QA4sjxLA99bD7QjbN&trim_start=2008-06-01&trim_end=2014-12-30&collapse=daily")
        response = response.json()

        if response['errors']:
            print( 'error:', response.error )
            continue

        if not response['data']:
            print( 'No data' )
            continue

        print( 'symbol:', symbol )

        for row in response['data']:
            entry = {}
            entry['symbol'] = symbol
            entry['date'] = row[0]
            entry['open_price'] = row[1]
            entry['high'] = row[2]
            entry['low'] = row[3]
            entry['close'] = row[4]
            entry['volume'] = row[5]
            entry['dividend'] = row[6]
            entry['split_ratio'] = row[7]

            Stock_history.objects.create( **entry )

        Stocks_Tracked.objects.create( 
            symbol=symbol,
            from_date=response["from_date"],
            to_date=response["to_date"],
            name=response['name'].split(" (")[0] )
seed()