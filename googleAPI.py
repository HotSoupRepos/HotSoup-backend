import requests

def test_api_query (lat, long, type, keyword):
    

    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{long}&radius=1500&type={type}&keyword={keyword}&key={YOUR-API-KEY-HERE}"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

test_api_query("41.18754","-73.2180112","food bank","food pantry")

