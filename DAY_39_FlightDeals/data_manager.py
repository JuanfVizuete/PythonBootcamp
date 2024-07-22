import requests
import os
from dotenv import load_dotenv
#from requests.auth import HTTPBasicAuth

load_dotenv()

USERNAME_SHEETY = os.getenv("USERNAME_SHEETY")
PROJECT_NAME = os.getenv("PROJECT_NAME")
SHEET_NAME = os.getenv("SHEET_NAME")

sheety_endpoint = f"https://api.sheety.co/{USERNAME_SHEETY}/{PROJECT_NAME}/{SHEET_NAME}"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.user = os.getenv("USER_SHEETY")
        self.password = os.getenv("PASSWORD_SHEETY")
        self.authorization = os.getenv("SHEETY_TOKEN")
        self.headers = {"Authorization": f"Basic {self.authorization}"}
        self.destination_data = {}

    def get_destination_data(self):
        sheet_response = requests.get(sheety_endpoint, headers=self.headers)
        sheet_data = sheet_response.json()
        self.destination_data = sheet_data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data,
                headers=self.headers
            )
            print(response.text)