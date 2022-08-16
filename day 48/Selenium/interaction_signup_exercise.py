from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service("C:\Development\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome_driver_path, options=op)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name_field = driver.find_element(by=By.NAME, value="fName")
last_name_field = driver.find_element(by=By.NAME, value="lName")
email_field = driver.find_element(by=By.NAME, value="email")
signup_button = driver.find_element(by=By.CLASS_NAME, value="btn-primary")

first_name_field.send_keys("Minh")
last_name_field.send_keys("Nguyen")
email_field.send_keys("minh.ng1003@gmail.com")
signup_button.click()
