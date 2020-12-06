import os
import time
from random import choice
from string import ascii_lowercase

from selenium import webdriver

alpha = list(ascii_lowercase)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'file.txt')
URL = 'http://suninjuly.github.io/file_input.html'

browser = webdriver.Chrome()
browser.get(URL)

inputs = browser.find_elements_by_xpath('//*[@type="text"]')
for inp in inputs:
    string = ''.join([choice(alpha) for _ in range(5)])
    inp.send_keys(string)

file_field = browser.find_element_by_id('file')
file_field.send_keys(FILE_PATH)

browser.find_element_by_css_selector('button.btn.btn-primary').click()

time.sleep(10)
browser.quit()



