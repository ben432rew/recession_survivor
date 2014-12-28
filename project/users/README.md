Users App
=========
Inputs/Outputs
--------------

Through the browser, a user will initially be able to:

    1. Sign Up
    2. Login
    3. Request password if they forgot it

Then, they will be taken to a welcome screen where they will be able to:

    1. See all time high scores list
    2. See their games history (through the games app)
    3. Continue a previous game/start a new one
    4. Change their password

Once they decide to start a new game or continue an old one, the user object will be available in views.py of any other apps as the 'request.user'.