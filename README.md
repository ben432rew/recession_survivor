Recession Survivor
==================
Putting the fun back in recession
---------------------------------

##Basic Functionality
Year is 2008, player starts with $10,000

Plays 12 Rounds

Every round shown how their stocks changed, user given choice of buying or selling stocks or just continuing with same portfolio

End of year all stocks are sold, display final balance


##Feature Upgrades
Add more years to be available to play

Every round, should be shown actual financial articles related to the stock they purchased from the prior month

Show high scores of all portfolios

Displaying trend of what happend to the stocks user actually bought

Different amounts of starting money


##Setup instructions

clone repository

set up venv

pip3 install django-toolbelt

pip3 install requests

pip3 install bcrypt

####postgres setup how-to

sudo su postgres

You should now be at the postgres user bash prompt

psql

You should now be in the psql prompt -> postgres=#

CREATE ROLE bears WITH login password 'bears';

ALTER ROLE bears WITH superuser createdb createrole;

\q

exit

now run createdb h_trader

go into the django shell and run: "from portfolio import seed" to get data in db

run pip3 freeze > requirements