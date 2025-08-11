# from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get('http://selenium.dev/')
# browser.maximize_window()

# title = browser.title
# print(f'Title of the page is: {title}')

# assert 'Selenium123' in title, "Title does not contain 'Selenium'"

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://selenium.dev/')

input("Press Enter to close the browser...")