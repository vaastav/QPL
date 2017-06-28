import requests
import json
from utility import uprint

# Retrieves data from the hard-coded url
# that contains the data
def get_data():
    response = requests.get("https://fantasy.premierleague.com/drf/bootstrap-static")
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    responseStr = response.text
    data = json.loads(responseStr)
    return data

