import time

from selenium import webdriver

browser = webdriver.Firefox()

browser.get("https://stepik.org/lesson/25969/step/8")

time.sleep(3)
browser.quit()
