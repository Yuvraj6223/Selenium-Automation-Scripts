

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://the-internet.herokuapp.com/iframe')

iframe = browser.find_element(By.ID, 'nce_0_ifr')
browser.switch_to.frame(iframe)

Text_editor = browser.find_element(By.ID, 'tinynce')
Text_editor.clear()
Text_editor.send_keys('Hello, this is a test message in the iframe.')
time.sleep(5)