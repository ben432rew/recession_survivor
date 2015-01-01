Historical Trader
==================
##Basic Functionality
Year is 2008, player starts with $10,000

Plays 12 Rounds

Every round shown how their stocks changed, user given choice of buying or selling stocks or just continuing with same portfolio

End of year all stocks are sold, display final balance


##Feature Upgrades
Add more years to be available to play (Great Depression?)

Every round, should be shown actual financial articles related to the stock they purchased from the prior month

Displaying trend of what happend to the stocks user actually bought

Different amounts of starting money


##Setup instructions

clone repository

set up venv

`pip3 install -r requirements.txt`

####postgres setup how-to

`sudo su postgres`

You should now be at the postgres user bash prompt

`psql`

You should now be in the psql prompt -> postgres=#

CREATE ROLE bears WITH login password 'bears';

ALTER ROLE bears WITH superuser createdb createrole;

\q

exit

Should be good to go

## Input and Outputs("v-" is a validation marker)
Portfolio Inputs-
portfolio: user_id
buy:portfolio_id, share-quantity, stock object
sell: portfolio_id, share_quantity, stock object
profit: portfolio_id
worth: portfolio_id
self-check: called by game each round and looks up all the stocks_owned tickers than checks the differences in the ticker prices in the Stock table for that day.

Portfolio Outputs-
buy:updates stock, v-can_buy?
sell: update stock, v-can_sell?
lookup: v-is_available?, price, low, high, volume, etc.
profit: worth + cash
worth: all stocks_owned prices sum
self-check: return messages based on activity, edit stocks based on findings

Game Inputs-
start_game: user_id
build portfolio: tickers, share amounts
next_round: game_id
endgame: game_id

Game Outputs-
start_game: game objects containing start balance, round, date, and portfolio form,
build portfolio: portfolio object
next_round: n/a
endgame: high score, balance

Stock Inputs-
get_price: ticker, date
get_general_finance_statements: ticker, date
get snippets_for_stock: ticker, date
get_snippets_for_date: date

Stock Outputs-
get_price: stock price
get_general_finance_statements: prevelant info
get_snippets_for_stock/date: sinppets

