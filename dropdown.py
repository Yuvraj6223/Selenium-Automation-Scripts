from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/dropdown')
driver.maximize_window()

dropdown_element = driver.find_element(By.ID, 'dropdown')
# select = Select(dropdown_element)
# # select.select_by_visible_text('Option 2')
# option_count = len(select.options)

# expected_count = 3
# if option_count == expected_count:
#     print('Test Passed: Dropdown has the expected number of options.')
# else:
#     print('Test Failed: Dropdown does not have the expected number of options.')

target_value = 'Option 3'
select = Select(dropdown_element)

for option in select.options:
    if option.text == target_value:
        option.click()
        print(f'Selected: {option.text}')
        break
    else:
        print(f'Option not found: {option.text}')