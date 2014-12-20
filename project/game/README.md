# Game app

## Start Game
Start game will only take optional arguments of starting balance(float), starting date(datetime) and a start portfolio(portfolio object).
The html view will allow the player to pick starting variables like; starting balance, starting date, and pick/ build a portfolio.
It allso display any current games the player may have saved to the data base and let them continue a incomplete game.


It will add a Game object to the users current session and redirect to the rounds. 
Start game will will return a http html/json response object 

## Rounds
This will not take any arguments, or output anything besides data to be rendered to the player
Each round will look in the current session for a Games object. if none is found the the player should be redirected to the start game page.
Once a Game object is found its portfolio object needs to be updated to from the last round date to the current round date.
Once the Portfolio object is updated, its relevant information can be displayed to the user.
At this point the user has options to;

1. Continue to the next round
2. Edit there portfolio
3. Save current game state
4. End current game

## End game
This will not take any arguments, or output anything besides data to be rendered to the player
When the user reaches the end of the game stars should be displayed and the players Game ranking displayed.
From here the player can goto the start game, or view the hi-scores.

## Hi-Scores
This will not take any arguments, or output anything besides data to be rendered to the player
This will just display the top 10 games, and maybe the users top game.

## Other
At the moment, I can not think of anything else that the Game app will need.
Please comment on this file if there anything that needs to be added, more clear or incorrect.
