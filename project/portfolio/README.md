# Portfolio
This app should work just like a regular portfolio, think what we did with the terminal trader app. Althou this app does not need to be fully built it, it should be. It will make our lives easier and make the game portion go smother.

## Templates

### Index
  This page should display a list of the current users portfolios and give links for each of them to delete, edit and manage( add/remove stocks) each portfolio. There should also be a link to create a new portfolio.
  * See display_all

### /create
  creates a new portfolio

### /display/(slugify title)
  This view should display the portfolio title and description, list all stocks and values, and total values. There should be links to manage, edit, and delete the current portfolio
  
### /edit/(slugify title)
  This view should allow the user edit the over portfolio, but not manage the stoks of the portfolio.
  
### /manage/(slugify title)
  This view allow a user to add and remove stocks from the current portfolio.
