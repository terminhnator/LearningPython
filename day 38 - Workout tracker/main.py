import requests
from datetime import datetime
import os

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

GENDER = "male"
WEIGHT_KG = 66
HEIGHT_CM = 163
AGE = 29

APP_ID = os.environ["NT_APP_ID"]
APP_KEY = os.environ["NT_APP_KEY"]

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("Tell me what you did today: ")

nutritionix_parameters = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, headers=nutritionix_headers, json=nutritionix_parameters)
result = response.json()
print(result)

sheety_endpoint = os.environ["NT_SHEET_ENDPOINT"]

sheety_headers = {
    "Authorization": os.environ["TOKEN"]
}

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

sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_headers)

print(sheet_response.text)
