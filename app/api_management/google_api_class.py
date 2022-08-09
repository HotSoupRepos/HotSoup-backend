import requests
import os
from dotenv import load_dotenv

load_dotenv()
#create your own .env file with your GOOGLE_MAP_API_KEY

GOOGLE_MAP_API_KEY=os.getenv("GOOGLE_MAP_API_KEY")

class Google_API:
    def get_locations_from_maps_api(lat, lng):
        type = "food bank"
        keyword = "food pantry"

        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius=3000&type={type}&keyword={keyword}&key={GOOGLE_MAP_API_KEY}"
        response = requests.get(url)

        if response.status_code == 200:
            status_code_200 = "sucessfully fetched the data with parameters provided"
            print(response.json())
            return status_code_200
        else:
            error_code_alternate = f"Hello person, there's a {response.status_code} error with your request"
            return error_code_alternate


    
