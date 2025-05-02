import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

my_password = "iybm ycey panx ldeh"
my_email = "thlorient@gmail.com"

# Your position is within +5 or -5 degrees of the ISS position.


def in_range(my_lat, my_long):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    lat_range = iss_latitude in range(round(my_lat)-5, round(my_lat)+5)
    long_range = iss_longitude in range(round(my_long)-5, round(my_long)+5)

    return lat_range and long_range


def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    return time_now >= sunset

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


while True:
    if in_range(MY_LAT, MY_LONG) and is_night():
        print("Sending email...")
        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email, msg=f"Subject: ISS Overhead!  \n\nLook UP! The ISS is overhead!")
    else:
        print("ISS not in range, waiting 1 min...")
    time.sleep(60)
