from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://demo.automationtesting.in/Resizable.html')
resize_element = browser.find_element(By.XPATH, "//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
Initial_element_size = browser.find_element(By.XPATH,"//div[@id='resizable']")
Initial_size = Initial_element_size.size
print("Initial size of the element:", Initial_size)
time.sleep(5)
action_chains = ActionChains(browser)
action_chains.click_and_hold(resize_element).move_by_offset(100, 100).release().perform()
time.sleep(5)
resized_element = Initial_element_size.size
print("Size of the element after resizing:", resized_element)
