from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://selenium.dev')

browser.switch_to.new_window('tab')
browser.get('https://playwright.dev')
number_of_tabs = len(browser.window_handles)
print(number_of_tabs)
current_tab = browser.current_window_handle

tabs_value = browser.window_handles
print(tabs_value)

browser.find_element(By.CSS_SELECTOR, '.getStarted_Sjon').click()
First_tab = browser.window_handles[0]
if current_tab != First_tab:
    browser.switch_to.window(First_tab)
browser.find_element(By.XPATH, "//span[normalize-space()='Downloads']").click()