import requests
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_MAP_API_KEY=os.getenv("GOOGLE_MAP_API_KEY")

def test_api_query (lat, long, type, keyword):
    

    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{long}&radius=3000&type={type}&keyword={keyword}&key={GOOGLE_MAP_API_KEY}"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

test_api_query("41.18754","-73.2180112","food bank","food pantry")

