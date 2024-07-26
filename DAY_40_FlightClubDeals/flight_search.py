import json

import requests
import os
from dotenv import load_dotenv

load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.api_key = os.getenv('AMADEUS_API_KEY')
        self.api_secret = os.getenv('AMADEUS_API_SECRET')
        self.token = self.get_new_token()

    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        code = "TESTING"
        return code

    def get_new_token(self):
        amadeus_token_endpoint = TOKEN_ENDPOINT
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret,
        }
        response = requests.post(url=amadeus_token_endpoint, headers=header, data=body)
        #print(f"Your token is {response.json()['access_token']}")
        #print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_cities_code(self, city_name):
        amadeus_cities_endpoint = IATA_ENDPOINT
        header = {
            "Authorization": f"Bearer {self.token}",
        }
        body = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(url=amadeus_cities_endpoint, params=body, headers=header)
        try:
            data = response.json()
            #print(data)
            code = data["data"][0]["iataCode"]
        except IndexError:
            print("Index Error: No airport code found")
            return "N/A"
        except KeyError:
            print("KeyError: No airport code found")
            return "Not Found"

        return code


    def get_flight_offer(self, destination_code, departure_time, return_time, origin_city_code, is_direct = True):
        if is_direct:
            is_direct = "true"
        else:
            is_direct = "false"

        header = {
            "Authorization": f"Bearer {self.token}",
        }
        body = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_code,
            "departureDate": departure_time,
            "returnDate": return_time,
            "adults": 1,
            "nonStop": is_direct,
            "currencyCode": "USD",
            "max": "10",
        }

        response = requests.get(url=FLIGHT_ENDPOINT, headers=header, params=body)
        try:
            data = response.json()
            print(json.dumps(data))
        except:
            print(f"check_flights() response code: {response.status_code}")
            return None

        return data
