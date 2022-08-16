import requests
from bs4 import BeautifulSoup


PRODUCT_URL = "https://www.amazon.com/Logitech-SUPERLIGHT-Ultra-Lightweight-Programmable-Compatible/dp/B087LXCTFJ"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.51 Safari/537.36",
    "Request Line": "GET / HTTP/1.1",
}

response = requests.get(url=PRODUCT_URL, headers=HEADERS)
product_webpage = response.text

soup = BeautifulSoup(product_webpage, "html.parser")
price = soup.find(name="span", class_="a-size-base a-color-price a-text-bold")

print(soup.prettify())

