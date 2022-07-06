from typing import Union

from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/locations")
async def get_all_locations():

    d = open('data.json')
    print(d)
    json_data = json.load(d)
    return json_data["localsoupkitchens"]


@app.get("/locations/{query}")
async def search_locations(query: str):

    d = open('data.json')
    print(d)
    json_data = json.load(d)
    return json_data["localsoupkitchens"][query.lower()]
