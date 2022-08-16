from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import random
from bs4 import BeautifulSoup
import requests

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8,vi;q=0.7"
}


response = requests.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.64136131503349%2C%22east%22%3A-122.30902488925224%2C%22south%22%3A37.53786642426611%2C%22north%22%3A37.850824527350326%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D", headers=header)
zillow_webpage = response.text

soup = BeautifulSoup(zillow_webpage, "html.parser")

listings_addresses = [address.get_text() for address in soup.select(".list-card-info a")]
listings_prices = [price.get_text() for price in soup.select(".list-card-price")]
listings_links = [link['href'] for link in soup.select(".list-card-info a")]

# print(listings_addresses)
# print(listings_prices)
# print(listings_links)

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
S = Service(CHROME_DRIVER_PATH)
OPTIONS = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=S, options=OPTIONS)
GOOGLE_FORM = "https://forms.gle/D55mREdwfGxSBur58"


for n in range(len(listings_links)):
    driver.get(GOOGLE_FORM)
    time.sleep(2)

    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address.send_keys(listings_addresses[n])
    price.send_keys(listings_prices[n])
    link.send_keys(listings_prices[n])

    submit_button.click()

