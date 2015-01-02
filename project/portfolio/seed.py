import requests
from portfolio.models import Stock_history, Stocks_Tracked
from pprint import pprint

symbols = [ 'KWR','GOOG', 'GOOGL', 'MSFT', 'FB', 'YHOO', 'ORCL', 'IBM', 'AAPL', 'BBY',
    'AMZN', 'GE', 'XOM', 'CVX', 'C', 'ED', 'CL', 'WSM', 'PG', 'K', 'HSY', 'DIS',
    'COH', 'ALL', 'GIS', 'CAG', 'KO', 'PEP', 'M', 'WHR', 'MKC', 'NKE',
    'SJM', 'WFM', 'AEO', 'RL', 'HD', 'GPS', 'UA', 'CSCO', 'BBBY', 'GM', 'F', 
    'BAC', 'WMT', 'COST', 'JNJ', 'MET', 'VZ', 'T' ]

# {"error":"Requested entity does not exist."} -- not tracked

def seed():
    for symbol in symbols:
        print( 'symbol:', symbol, "===========" )

        # todaye = str( datetime.date.today() )

        if Stocks_Tracked.objects.filter( symbol=symbol ).exists():
            print( "all ready tracked" )
            continue

        response = requests.get("https://www.quandl.com/api/v1/datasets/WIKI/"+ symbol +".json?auth_token=M-1QA4sjxLA99bD7QjbN&trim_start=2008-06-01&trim_end=2014-12-30&collapse=daily")
        response = response.json()


        if response['errors']:
            print( 'error:', response['errors'] )
            continue

        if not response['data']:
            print( 'No data' )
            continue

        for row in response['data']:
            entry = {
                'symbol': symbol,
                'date': row[0],
                'open_price': row[1],
                'high': row[2],
                'low': row[3],
                'close': row[4],
                'volume': row[5],
                'dividend': row[6],
                'split_ratio': row[7]
            }

            try:
                Stock_history.objects.create( **entry )
            except:
                print( "??" )
                pprint( entry )

        Stocks_Tracked.objects.create( 
            symbol=symbol,
            from_date=response["from_date"],
            to_date=response["to_date"],
            name=response['name'].split( " (" )[0]
        )
seed()
