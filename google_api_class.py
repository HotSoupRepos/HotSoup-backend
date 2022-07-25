import googleAPI
import requests

class Google_API:
    def Maps_API_Request(self, api, parameters, lat, long, type, keyword):
        parameters = {
            lat: "lat",
            long: "long",
            type: "type",
            keyword: "keyword"
        }
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{long}&radius=3000&type={type}&keyword={keyword}&key={GOOGLE_MAP_API_KEY}"
        response = requests.get(url, params=parameters)
        if response.status_code == 200:
            print("sucessfully fetched the data with parameters provided")
            self.formatted_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")
