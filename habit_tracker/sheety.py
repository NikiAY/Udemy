import requests
import datetime

TOKEN = "Bearer thisisshuchacrazytokenisweartogodbro"
# response = requests.get(url= sheety_endpoint)
# print(response.json())

now = datetime.datetime.now()
time = now.strftime("%X")
date = now.strftime("%x")

id = 4

sheety_endpoint = f"https://api.sheety.co/1ad3c57a699300a7b751459a597864fc/udemyMyWorkouts/workouts/{id}"

headers = {
    "Authorization": TOKEN,
}
data = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": "Swimming",
        "duration": "15",
        "calories": 133
    }
}

# response = requests.put(url= sheety_endpoint, json= data, headers= headers)
# print("response.status_code =", response.status_code) 
# print("response.text= ", response.text)