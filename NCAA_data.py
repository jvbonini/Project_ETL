from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import pymongo
import os

# Setup connection to mongodb
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Select database and collection to use
db = client.NCAA_data
collection = db.produce

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

# Create NCAA player stats global dictionary that can be imported into Mongo
NCAA_info = {}

def player_stats():

    player_stats_url = 'https://www.ncaa.com/stats/lacrosse-women/d1'

     # Use Panda's `read_html` to parse the url
    player_stats = pd.read_html(player_stats_url)

      # Find the player stats DataFrame in the list of DataFrames as assign it to `player_stats_df`
    player_stats_df = player_stats[0]

    # Assign the columns 
    player_stats_df.columns = ['Rank','Name', 'Team', 'Per Game']

    # Set the index to the (player) `Name` column without row indexing
    player_stats_df.set_index('Name', inplace=True)

    team_stats_df = player_stats_df.set_index('Team', inplace=True)

    # Save html code to folder Assets
    player_data = player_stats_df.to_html()
    team_data = team_stats_df.to_html()

    # Dictionary entry from player_stats
    NCAA_info['player_stats'] = player_data
    NCAA_info['team stats']= team_data

    return NCAA_info


