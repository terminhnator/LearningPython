from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service("C:\Development\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome_driver_path, options=op)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

count_articles = driver.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]')
# count_articles.click()

all_portals = driver.find_element(by=By.LINK_TEXT, value="All portals")
all_portals.click()

search = driver.find_element(by=By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


# driver.close()
# driver.quit()
