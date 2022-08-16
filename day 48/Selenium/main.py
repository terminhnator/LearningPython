from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = Service("C:\Development\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome_driver_path, options=op)

driver.get("https://www.python.org/")
scraped_event_times = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
scraped_event_names = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget .menu a")
event_times = [date.text for date in scraped_event_times]
event_names = [event.text for event in scraped_event_names]
event_dict = {}

for n in range(len(event_times)):
    event_dict[n] = {
        "time": event_times[n],
        "name": event_names[n]
    }

print(event_dict)
# driver.close()
driver.quit()
