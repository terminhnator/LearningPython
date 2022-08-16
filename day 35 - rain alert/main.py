import requests
from twilio.rest import Client

account_sid = "AC689f9dc001a7064ecf05ed7af2ad58ad"
auth_token = "abdb2132aa695da133081e314fab3e4c"
vn_lat = 10.801103
vn_lon = 106.749156
palembang_lat = -2.976074
palembang_lon = 104.775429

weather_parameters = {
    "lat": palembang_lat,
    "lon": palembang_lon,
    "exclude": "current,minutely,daily",
    "appid": "8a93ac72810f84e95f9fb82e0af52430"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
hourly_weather_data = weather_data["hourly"][0:12]

will_rain = False

for _ in hourly_weather_data:
    condition = hourly_weather_data[0]["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella!",
        from_="+19362431743",
        to="+84906771508")

print(message.status)
