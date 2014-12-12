Recession Survivor
==================
Putting the fun back in recession
---------------------------------

##Basic Functionality
Year is 2008, player starts with $100,000

Plays 12 Rounds

Every round shown how their stocks changed, user given choice of buying or selling stocks or just continuing with same portfolio

End of year all stocks are sold, display final balance

Need to store all the data from first day of every month in database because if there are many users on a real web app, making a bunch of api calls is a no-no.  Here's an api we could pull the data from: [Quandl](https://www.quandl.com/WIKI)

####Database schema:
Users (we'll use the django user built-in)

Transaction History
    *user id
    *symbol
    *number of shares
    *date
    *account change

Stocks
    *user id
    *symbol
    *shares
    *price bought at
    *date bought at

Portfolios (Final Scores):
    *user id
    *final score
    *date played

##Feature Upgrades
Add more years to be available to play

Every round, should be shown actual financial articles related to the stock they purchased from the prior month

Show high scores of all portfolios

Displaying trend of what happend to the stocks user actually bought


##Schedules
Devon not available after noon on sunday
Benny not available Saturday after 2pm