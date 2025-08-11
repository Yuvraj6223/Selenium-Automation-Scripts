from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
implicit_wait = 10
driver.implicitly_wait(implicit_wait)
driver.maximize_window()

driver.get('https://saucedemo.com/')
driver.find_element(By.ID, "user-name").send_keys('standard_user')
driver.find_element(By.ID, "password").send_keys('secret_sauce')
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()
