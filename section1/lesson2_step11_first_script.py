import os
import time

from selenium import webdriver


browser = webdriver.Chrome()

time.sleep(5)

browser.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

textarea = browser.find_element_by_css_selector(".textarea")

textarea.send_keys("get()")
time.sleep(5)

submit_button = browser.find_element_by_css_selector(".submit-submission")

submit_button.click()
time.sleep(5)

browser.quit()