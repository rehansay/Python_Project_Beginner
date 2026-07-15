import requests
import json
import win32com.client as wincom

speak=wincom.Dispatch("SAPI.SpVoice")

city=input("Enter the name of the city\n")

url=f"https://api.weatherapi.com/v1/current.json?key=9f478f52ae524eb2861130033261507&q={city}"

r=requests.get(url)
# print (r.text)
data=json.loads(r.text)
temp=data["current"]["temp_c"]
feelsLike=data["current"]["feelslike_c"]
condition=data["current"]["condition"]["text"]

message=f"The current tempratur in {city} is {temp} degrees Celsius and it feels like {feelsLike} celsius with {condition}" 
speak.Speak(message)

# print(f"\n📍 City: {data['location']['name']}")
# print(f"🌍 Country: {data['location']['country']}")
# print(f"🌡️ Temperature: {data['current']['temp_c']}°C")
# print(f"🤒 Feels Like: {data['current']['feelslike_c']}°C")
# print(f"☁️ Condition: {data['current']['condition']['text']}")
# print(f"💧 Humidity: {data['current']['humidity']}%")
# print(f"💨 Wind: {data['current']['wind_kph']} km/h")