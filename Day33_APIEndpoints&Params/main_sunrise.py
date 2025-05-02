import requests
import datetime as dt

parameters = {
    "lng": 40.712776,
    "lat": -74.005974,
    "formatted": 0
}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()["results"]
print(data)
sunrise = data["sunrise"].split("T")[1].split(":")[0]
sunset = data["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = dt.datetime.now()
print(time_now.hour)
