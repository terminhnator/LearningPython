import requests
import datetime
from twilio.rest import Client

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
day_before_yesterday = yesterday - datetime.timedelta(days=1)

STOCK = "HOOK"
COMPANY_NAME = "HOOKIPA Pharma Inc."
AV_API_KEY = "VP96U25K7NVC7D59"
NEWSAPI_API_KEY = "efb98800fcac4397a01b8b380ec0600b"
TWILIO_SID = "AC689f9dc001a7064ecf05ed7af2ad58ad"
TWILIO_AUTH_TOKEN = "abdb2132aa695da133081e314fab3e4c"

av_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AV_API_KEY
}

newsapi_parameters = {
    "apiKey": NEWSAPI_API_KEY,
    "qInTitle": COMPANY_NAME,
    "sortBy": "publishedAt",
    "language": "en"
}

response_av = requests.get(url="https://www.alphavantage.co/query", params=av_parameters)
response_av.raise_for_status()
yesterday_data = float(response_av.json()["Time Series (Daily)"][str(yesterday)]["4. close"])
day_before_yesterday_data = float(response_av.json()["Time Series (Daily)"][str(day_before_yesterday)]["4. close"])

difference_between_2_days = float(("{:.2f}".format((yesterday_data / day_before_yesterday_data - 1) * 100)))
print(difference_between_2_days)

up_down = None
if difference_between_2_days > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if difference_between_2_days > 5 or difference_between_2_days < -5:

    response_newsapi = requests.get(url="https://newsapi.org/v2/everything", params=newsapi_parameters)
    response_newsapi.raise_for_status()
    articles = response_newsapi.json()["articles"][0:3]
    formatted_articles = [f"{STOCK}: {up_down}{difference_between_2_days}%\nHeadline: {article['title']}. \nBrief:{article['description']}" for article in articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(body=article,
                                         from_="+19362431743",
                                         to="+84978332293"
                                         )
