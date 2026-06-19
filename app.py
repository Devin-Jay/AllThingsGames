#app.py

# import libraries
from dotenv import load_dotenv
import os
from requests import post
# from nicegui import ui

# load environment variables
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

response = post('https://api.igdb.com/v4/game_engines', **{'headers': {'Client-ID': CLIENT_ID, 'Authorization': f'Bearer {ACCESS_TOKEN}'},'data': 'fields name; limit 500; where name = *"Unity"*;'})

for game_engine in response.json():
    print(game_engine)
    print()
