import requests
import json
from utility import uprint
from parsers import *

# Retrieves data from the hard-coded url
# that contains the data
def get_data():
    response = requests.get("https://fantasy.premierleague.com/drf/bootstrap-static")
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    responseStr = response.text
    data = json.loads(responseStr)
    return data

def get_individual_player_data(player_id):
    base_url = "https://fantasy.premierleague.com/drf/element-summary/"
    full_url = base_url + str(player_id)
    response = requests.get(full_url)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return data

def parse_data(data):
    #parse_players(data["elements"])
    # TODO: parse other stats that may be useful
    num_players = len(data["elements"])
    for i in range(num_players):
        player_data = get_individual_player_data(i+1)
        parse_player_history(player_data["history_past"], i+1)
        parse_player_gw_history(player_data["history"], i+1)

data = get_data()
parse_data(data)
