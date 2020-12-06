import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()

try:
    browser.get('http://suninjuly.github.io/simple_form_find_task.html')
    first_name = browser.find_element(By.TAG_NAME, 'input')
    first_name.send_keys('Ivan')

    last_name = browser.find_element(By.NAME, 'last_name')
    last_name.send_keys('Petrov')

    city = browser.find_element(By.CLASS_NAME, 'city')
    city.send_keys('Smolensk')

    country = browser.find_element(By.ID, 'country')
    country.send_keys('Russia')

    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit.click()


finally:
    time.sleep(30)
    browser.quit()
