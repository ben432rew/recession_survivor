Historical Trader
==================

[Try it out](http://ht.wmantly.info)


##The Game:
Once a user signs up, they are able to start a game.

At the beginning of the game, they choose the amount of money they are to build an initial portfolio with.

They also choose the timeframe for the game: From what date to what date, and how often the game rounds happen (weekly, monthly, or yearly).

**Then the game begins.**

Each round, the user can look up the new stock prices for that day in history, and can choose to buy or sell shares.

At the end of the last round, all of the user's shares are sold and their final score is their total cash balance they have.


##Setup instructions

clone repository

set up venv

`pip3 install -r requirements.txt`

####postgres setup how-to

`sudo su postgres`

You should now be at the postgres user bash prompt

`psql`

You should now be in the psql prompt -> postgres=#

`CREATE ROLE bears WITH login password 'bears';`

`ALTER ROLE bears WITH superuser createdb createrole;`

`\q`

`exit`

Then, to seed the database with the historical stocks:

`psql h_trader < h_trader_portfolio_stock_history.pg`

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

