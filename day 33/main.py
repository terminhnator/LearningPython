import requests
import smtplib
from datetime import datetime
import time

MY_LAT = 10.801099
MY_LNG = 106.749198
MY_EMAIL = "terminhnator.1003@gmail.com"
MY_PASSWORD = "1Yz9j%R7Pr4@"


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


def check_range():
    if 5 <= iss_latitude <= 15 and 101 <= iss_longitude <= 111:
        return True
    else:
        return False


def check_night():
    if sunset <= time_now or time_now <= sunrise:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if check_range() and check_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="minh.ng1003@gmail.com",
                msg=f"Subject:The ISS is right above you!\n\nLook up son!"
                                )
