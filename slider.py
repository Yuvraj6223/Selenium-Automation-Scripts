from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time



browser = webdriver.Chrome()
browser.get('https://the-internet.herokuapp.com/horizontal_slider')
time.sleep(5)

slider = browser.find_element(By.XPATH, '//input[@type="range"]')
actions = ActionChains(browser)
actions.click_and_hold(slider).move_by_offset(50, 0).release().perform()
time.sleep(5)
browser.quit()