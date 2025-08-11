
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://the-internet.herokuapp.com/javascript_alerts'
browser.get(url)

alert_button = browser.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
time.sleep(2)
alert_button.click()

# Switch to alert and accept it
time.sleep(2)
alert = browser.switch_to.alert
print("Alert text:", alert.text)
alert.accept()

time.sleep(2)
browser.quit()
