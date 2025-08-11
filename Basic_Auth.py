from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



username = 'admin'
password = 'admin'

driver = webdriver.Chrome()
driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')
time.sleep(10)