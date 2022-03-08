import requests as r, json

base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "39a54b32b608837afb449c9d1bb49ae2"

cityname = input("What city would you like to visit?\n")
answer = input(f"Would you like details about {cityname}?\n")

url = f"{base_url}q={cityname}&appid={api_key}"
response = r.get(url) #accessing data
data = response.json() #saving the weather details in a json file
print()

try:
    if answer == "yes":
        if response.status_code == 200:

            #name
            name = data['name']
            print(f"-----Showing details for {name}-----")

            #coordinates
            coordinates = data['coord']
            long = coordinates['lon']
            lat = coordinates['lat']
            print(f"{name} is located in latitude:{lat} and longitude:{long}")

            #extrating temperature
            main = data['main']
            temp_in_k = main['temp']
            temp_in_c = (temp_in_k - 273.15)
            if temp_in_c > 33 and temp_in_c < 42:
                print(f"{name} is quite hot now")
            elif temp_in_c > 22 and temp_in_c < 32:
                print(f"{name} is warm")
            else:
                print(f"{name} is cold at the moment")
            print(f"It is currently {round(temp_in_c)}°C in {name}")

            #humidity
            humidity = main['humidity']
            print(f"The humidity in {name} is {humidity}%")

            #about the clouds
            weather = data['weather']
            weather_without_list = weather[0]
            description = weather_without_list['description']
            print(f"{name} has {description}")
        else:
            print("Sorry, there is an error in the HTTP request", "\N{confused face}")

    else:
        print("Goodbye")

except:
    print("Have you entered a valid city name?")
