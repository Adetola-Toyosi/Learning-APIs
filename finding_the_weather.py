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

#indexing
main = weather_data['main']
print(main['temp'])
print(main['humidity'])

print(weather_data['name'])

coordinates = weather_data['coord']
longitude = coordinates['lon']
latitude = coordinates['lat']

weather = weather_data['weather']
weather_without_list = weather[0]
print(weather_without_list['description'])

