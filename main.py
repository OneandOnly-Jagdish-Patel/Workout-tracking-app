
import requests
import json
from datetime import datetime
import os
import pprint

GENDER = "male"
WEIGHT_KG = "52"
HEIGHT_CM = "143"
AGE = "18"

APP_ID = "You can get this from nutritionix api"
API_KEY = "You can get this from nutritionix api"

env_var = os.environ
pprint.pprint(dict(env_var),width=1)
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

for results in result["exercises"]:
    excercise1 = results["user_input"]
    duration_time = results["duration_min"]
    calories_burnt = results["nf_calories"]
    today = datetime.now().strftime("%d/%m/%Y")

    now = datetime.now()
    time_now = now.strftime("%H:%M:%S")
    api_id = "You can get this from sheety api"


    row_2 = {
        "sheet1":{
        "date": today,
        "time": time_now,
        "excercise": excercise1,
        "duration": duration_time,
        "calories": calories_burnt
        }
    }

    token_id = {
        "Authorization":"Bearer this_is_secreat"
    }

    data2 = requests.post(url = api_id,json = row_2,headers= token_id)
    print(data2.text)

