from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome ()
browser.maximize_window()
browser.get('https://the-internet.herokuapp.com/drag_and_drop') 
source_element = browser.find_element(By.ID, "column-a") 
destination_element = browser.find_element(By.ID,  "column-b") 
actions = ActionChains(browser)
actions.drag_and_drop(source_element, destination_element).perform()
time.sleep(5)