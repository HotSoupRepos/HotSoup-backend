import googleAPI
import requests

try:
    import json
except ImportError:  # pragma: no cover
    # For older versions of Python.
    import data.json as json

try:
    from urllib import urlencode
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.parse import urlencode

try:
    from urllib2 import urlopen
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.request import urlopen

from xml2dict import xml2dict


class Google_API:
    def maps_api_request(self, parameters, lat, long, type, keyword):
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


    def check_url(self):
        url = self.url
        if(url and url.endswith('/')):
            url = url.rstrip('/')
            self.url = url


    def format_api_data_to_json(self, output_format, data):
        if output_format:
            output_format = output_format.lower()
        elif output_format == 'json':
            return json.loads(data)
        return data
    
