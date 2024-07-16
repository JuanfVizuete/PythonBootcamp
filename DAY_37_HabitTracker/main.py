import requests
from datetime import date, datetime
import os


USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
GRAPH = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#Create account
#response = requests.post(url=pixela_endpoint, json=user_parameters)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH,
    "name": "Study Graph",
    "unit": "min",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

#Create graph
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

post_pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"

today = date.today().strftime("%Y%m%d")
#today = datetime(2024, 7, 15).strftime("%Y%m%d")
print(today)

pixel_parameters = {
    "date": today,
    "quantity": input("How many minutes did you study today? "),
}

#Post a pixel
response = requests.post(url=post_pixel_endpoint, json=pixel_parameters, headers=headers)
print(response.text)


update_pixel_endpoint = f"{post_pixel_endpoint}/{pixel_parameters['date']}"

pixel_upd_parameters = {
    "quantity": "80",
}

#Update a pixel
# response = requests.put(url=update_pixel_endpoint, json=pixel_upd_parameters, headers=headers)
# print(response.text)


delete_pixel_endpoint = f"{post_pixel_endpoint}/{pixel_parameters['date']}"

#Delete a pixel
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)

