from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

PROMISED_DOWN = 160
PROMISED_UP = 160
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
S = Service(CHROME_DRIVER_PATH)
OPTIONS = webdriver.ChromeOptions()
DRIVER = webdriver.Chrome(service=S, options=OPTIONS)

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = DRIVER
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(7)
        go_button = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        sleep(60)
        self.down = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        print(self.down.text)
        print(self.up.text)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com")
        sleep(7)
        login_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        login_button.click()
        sleep(5)
        google_signin_button = self.driver.find_element(by=By.XPATH, value='//*[@id="gsi_329286_606896"]')
        google_signin_button.click()

bot = InternetSpeedTwitterBot(DRIVER)
bot.get_internet_speed()
bot.tweet_at_provider()

