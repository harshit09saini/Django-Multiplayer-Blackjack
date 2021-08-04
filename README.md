# ♣ Multiplayer Blackjack ♣

This is a multiplayer version of the famous card game, Blackjack. Autheticated players can create or join a room to play 
the game with another opponent over a network.

## Demo


https://user-images.githubusercontent.com/52451723/128008867-601a95d1-0ea4-47f9-b862-ababd715820e.mp4


## Install 
### To Run Locally

Create a virtual environment for the django app. 

```
pip install virtualenvwrapper-win
```

Create a virtual environment 
```
mkvirtualenv django-blackjack
```
Switch to the virtual environment
```
workon django-blackjack
```

Now, you can install the required project dependencies
```
pip install requirements.txt
```

Install a [redis server]("https://redis.io/download")

To run the app, 
```
python manage.py runserver
```

