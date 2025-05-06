import requests
from pprint import pprint
from twilio.rest import Client


api_key = "2fafe5e62d03835c7d76b4e23bb857fe"
lat = "32.700809"
long = "-103.136208"
endpoint = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = "ACb173e7580d5c5d64a1205127006f7dbd"
auth_token = "0655bb97bb456da18ca2599a5547a73e"

parameters = {
    "lat": lat,
    "lon": long,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(
    url=endpoint, params=parameters)
response.raise_for_status()
weather_data = ["Rain" for i in response.json()["list"]
                if i["weather"][0]["id"] < 800]
pprint(weather_data)

if "Rain" in weather_data:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_="+16066442593",
        to="+525521868386",
    )
    print(message.status)
else:
    print("Wont rain")
