import requests
import os
from dotenv import load_dotenv

load_dotenv()
#create your own .env file with your GOOGLE_MAP_API_KEY

GOOGLE_MAP_API_KEY=os.getenv("GOOGLE_MAP_API_KEY")
#use own API KEY from google cloud account - will consolidate to business api at later date

def test_api_query (lat, long, type, keyword):
    

    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{long}&radius=3000&type={type}&keyword={keyword}&key={GOOGLE_MAP_API_KEY}"
    #default to 20 add parameter token to get up to 60 search results 

    payload={}
    headers = {}
    data = {
        "lat": 41.1772347,
        "lng": -73.2180112,
        "address": "1067 Park Ave Bridgeport CT 06604",
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    response = requests.post("POST", url, json=data, headers=headers, data=payload)

    print(response.text)
    print("Status Code", response.text)

test_api_query("41.18754","-73.2180112","food bank","food pantry")
#test with long, lat, type, and keyword
