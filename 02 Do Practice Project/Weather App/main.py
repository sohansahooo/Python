import requests
import json
import pyttsx3

engine = pyttsx3.init()

city = input("Enter a city name: ")
menu = '''Weather Informations (Enter one of the numbers) 
1. Region
2. Country
3. Latitude 
4. Longitude
5. Local Time
6. Temperature (C) 
7. Temperature (F) 
8. Condition
9. Wind Speed (km/h)
10. Humidity
11. UV Index
12. Visibility (km)
13. Exit'''
print(menu)
choice = int(input("Enter your choice: "))

url = f"https://api.weatherapi.com/v1/current.json?key=0f9d885ad2994505b0952128240912&q={city}"

response = requests.get(url)
wdic = json.loads(response.text)

def get_weather_info(choice, data):
    match choice:
        case 1:
            return f"The region of {city} is {data['location']['region']}."
        case 2:
            return f"The country of {city} is {data['location']['country']}."
        case 3:
            return f"The latitude of {city} is {data['location']['lat']}."
        case 4:
            return f"The longitude of {city} is {data['location']['lon']}."
        case 5:
            return f"The local time in {city} is {data['location']['localtime']}."
        case 6:
            return f"The temperature in {city} is {data['current']['temp_c']} °C."
        case 7:
            return f"The temperature in {city} is {data['current']['temp_f']} °F."
        case 8:
            return f"The weather condition in {city} is {data['current']['condition']['text']}."
        case 9:
            return f"The wind speed in {city} is {data['current']['wind_kph']} km/h."
        case 10:
            return f"The humidity in {city} is {data['current']['humidity']}%."
        case 11:
            return f"The UV index in {city} is {data['current']['uv']}."
        case 12:
            return f"The visibility in {city} is {data['current']['vis_km']} km."
        case 13:
            return "Exiting program..."
        case _:
            return "Invalid choice! Please select a number from the menu."

info = get_weather_info(choice, wdic)
print(info)
engine.say(info)
engine.runAndWait()

if choice == 13:
    print("Goodbye!")
    engine.say("Goodbye!")
    engine.runAndWait()
