import requests
from datetime import date, datetime
import os

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']

USERNAME_SHEETY = os.environ['USERNAME_SHEETY']
PROJECT_NAME = "myWorkoutsJv"
SHEET_NAME = "workouts"
SHEETY_TOKEN = os.environ['SHEETY_TOKEN']

WEIGHT_KG = 65
HEIGHT_CM = 180
AGE = 27

url = "https://trackapi.nutritionix.com"
exercise_endpoint = f"{url}/v2/natural/exercise"

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}


# response = requests.get(url, headers=headers)
# response.raise_for_status()
# print(response.text)

parameters = {
    "query": input("Tell me which exercise you did: "),
    #"query": "ran for 2km and walked for 3km",
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

def camelCase(word):
    word = word.title()
    word[0] = word[0].lower()
    return word

def postWorkoutData():
    # Post in Nutritionix for getting the Exercise details
    response = requests.post(exercise_endpoint, headers=headers, json=parameters)
    response.raise_for_status()
    result = response.json()
    print(result)
    today_date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%X")

    sheety_header = {
        "Authorization": f"Basic {SHEETY_TOKEN}",
    }

    sheety_endpoint = f"https://api.sheety.co/{USERNAME_SHEETY}/{PROJECT_NAME}/{SHEET_NAME}"

    for exercise in result["exercises"]:
        sheet_inputs = {
            "workout": {
                "date": today_date,
                "time": now_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }

        sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=sheety_header)

        print(sheet_response.text)


postWorkoutData()