import requests
import datetime
from privates import *


today = datetime.datetime.now()

GENDER = GENDER
WEIGHT = WEIGHT
HEIGHT = HEIGHT
AGE = AGE

APP_ID = APP_ID
API_KEY = API_KEY

query = input("What excercise did you do? ")

headers = {
    "content-type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

parameters = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,


}
language_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


#####Sheeety Part######

BEARER_TOKEN = BEARER_TOKEN

sheety_headers = {
    "Authorization": BEARER_TOKEN,

}

response = requests.post(url=language_endpoint, json=parameters, headers=headers)
result = response.json()

#print(result)
#print(result["exercises"][0]["name"])

sheet_url = "https://api.sheety.co/175d9ba06fa649a07d38ee189b356b35/workoutV2/sheet1"

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    row_addition = requests.post(url=sheet_url, json=sheet_inputs, headers=sheety_headers)
    print(row_addition.text)
