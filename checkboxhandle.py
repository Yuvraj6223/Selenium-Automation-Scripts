from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
checkboxes = driver.find_element(By.ID, 'RESULT_CheckBox-7')
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)
    
checked_count = 0
for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count += 1
        
expected_count = 7
if checked_count == expected_count:
    print(f"Test Passed: {checked_count} checkboxes are checked as expected.")
else:
    print(f"Test Failed: Expected {expected_count} checkboxes to be checked, but found {checked_count}.")
    
driver.close()