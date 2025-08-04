import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def get_access_token():
    API_KEY = os.environ.get('AMADEUS_API')
    API_SECRET = os.environ.get('AMADEUS_SECRET')
    url_request_token = 'https://test.api.amadeus.com/v1/security/oauth2/token'
    headers1 = {
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type":"client_credentials",
        "client_id": API_KEY,
        "client_secret": API_SECRET
    }
    res = requests.post(url_request_token, headers=headers1, data=data)

    return res.json()['access_token']

def search_flights(depatureIataCode, arrievalIataCode, yyyymmddDate, adults=1):
    base_url = "https://test.api.amadeus.com/v2"
    querystring = {
        "originLocationCode": depatureIataCode,
        "destinationLocationCode": arrievalIataCode,
        "departureDate": yyyymmddDate,
        "adults": adults,
    }
    headers = {
        "Authorization": f'Bearer {get_access_token}'
    }

    response = requests.get(f'{base_url}/shopping/flight-offers', params=querystring, headers=headers)
    data2 = response.json()

    print(json.dumps(data2, indent=4, ensure_ascii=False))