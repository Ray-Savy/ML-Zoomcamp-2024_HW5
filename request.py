import requests


url = 'http://localhost:5555/predict'

client = {"job": "management", "duration": 400, "poutcome": "success"}
resp = requests.post(url, json=client).json()

print(resp)
