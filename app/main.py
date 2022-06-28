from typing import Union

from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/locations/{location_id}")
async def read_item(location_id: int, q: Union[str, None] = None):

    f = open('sample_locations.json')
    json_data = json.load(f)
    return json_data[str(location_id)]