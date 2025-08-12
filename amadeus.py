import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def get_access_token():
    API_KEY = os.environ.get('AMADEUS_API')
    API_SECRET = os.environ.get('AMADEUS_SECRET')
    url_request_token = f'https://test.api.amadeus.com/v1/security/oauth2/token'
    headers1 = {
        "Content-Type" : "application/x-www-form-urlencoded",
        # "Authorization": "Bearer TOKEN"
    }
    
    data = {
        "grant_type":"client_credentials",
        "client_id": API_KEY,
        "client_secret": API_SECRET
    }
    res = requests.post(url_request_token, headers=headers1, data=data)

    return res.json()['access_token']

def search_flights(params):
    base_url = "https://test.api.amadeus.com/v2"
    
    params['max'] = 3

    headers = {
        "Authorization": f'Bearer {get_access_token()}'
    }

    response = requests.get(f'{base_url}/shopping/flight-offers', params=params, headers=headers)

    return response.json()

# if __name__ == '__main__':
    # print(search_flights({
    #     "originLocationCode": "NYC",
    #     "destinationLocationCode": "LAX",
    #     "departureDate": "2023-12-01",
    #     "adults": 1
    # }))