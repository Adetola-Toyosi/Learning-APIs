import requests
import json

endpoint = "https://api.openweathermap.org/data/2.5/weather?"
cityname = "Hyderabad"
api_key = "39a54b32b608837afb449c9d1bb49ae2"

url = f"{endpoint}q={cityname}&appid={api_key}"
print(requests.get(url))