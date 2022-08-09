from email.headerregistry import Address
from pydantic import BaseModel

from fastapi import FastAPI
import json

from app.api_management.google_api_class import Google_API as google_api

app = FastAPI()

class User(BaseModel):
    lat: float
    lng: float

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/locations/")
async def get_all_locations():

    d = open('data.json')
    json_data = json.load(d)
    return json_data["localsoupkitchens"]


@app.get("/locations/{query}")
async def search_locations(query: str):

    d = open('data.json')
    
    json_data = json.load(d)
    return json_data["localsoupkitchens"][query.lower()]


@app.post("/locations/", response_model=User)
async def search_locations(user: User):
    locations = google_api.get_locations_from_maps_api(user.lat, user.lng)
    return locations


