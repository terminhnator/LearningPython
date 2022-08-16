from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import random

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
S = Service(CHROME_DRIVER_PATH)
OPTIONS = webdriver.ChromeOptions()
DRIVER = webdriver.Chrome(service=S, options=OPTIONS)
SIMILAR_ACCOUNT = "chowpuppies"
USERNAME = "minh.ng1003@gmail.com"
PASSWORD = "r!jSU^uWMS56"


class InstaFollower:
    def __init__(self):
        self.driver = DRIVER

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        username_input = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(USERNAME)
        password_input = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(PASSWORD)
        time.sleep(3)
        password_input.send_keys(Keys.ENTER)

        time.sleep(3)
        not_now_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_button.click()

        time.sleep(6)
        no_notifications_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div/div/div[3]/button[2]')
        no_notifications_button.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        followers_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')
        followers_button.click()
        time.sleep(2)
        followers_popup = self.driver.find_element(by=By.XPATH, value='/html/body/div[6]/div/div')
        time.sleep(5)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)

    def follow(self):
        followers_list = self.driver.find_elements(by=By.CSS_SELECTOR, value='li button')
        for follower in followers_list:
            try:
                follower.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

