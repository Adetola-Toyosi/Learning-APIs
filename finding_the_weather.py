import requests as r
import json

endpoint = "https://api.openweathermap.org/data/2.5/weather?"
cityname = "Hyderabad"
api_key = "39a54b32b608837afb449c9d1bb49ae2"

url = f"{endpoint}q={cityname}&appid={api_key}"
response = r.get(url)

#print(response.text)
#print(url) #to see the url and open in a web browser

weather_data = response.json()
with open('weather.json', 'w') as file:
    json.dump(weather_data, file)
