# https://stepik.org/lesson/138920/step/5?unit=196194
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Example:
    def __init__(self):
        self.url = 'https://www.degreesymbol.net/'
        self.browser = webdriver.Chrome()

    def open_page(self):
        self.browser.get(self.url)

        # Full match
        # link = browser.find_element_by_link_text('» Degree symbol examples')

        # partial match
        link = self.browser.find_element_by_partial_link_text('examples')

        link.click()
        time.sleep(5)

        self.browser.quit()


class Lesson:
    def __init__(self):
        self.url = 'http://suninjuly.github.io/find_link_text'
        self.browser = webdriver.Chrome()

    def open_link_by_text(self, link_text=None):
        self.browser.get(self.url)
        if not link_text:
            link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

        self.link = self.browser.find_element_by_link_text(f'{link_text}')
        self.link.click()

    def fill_the_form(self):
        try:
            first_name = self.browser.find_element(By.TAG_NAME, 'input')
            first_name.send_keys('Ivan')

            last_name = self.browser.find_element(By.NAME, 'last_name')
            last_name.send_keys('Petrov')

            city = self.browser.find_element(By.CLASS_NAME, 'city')
            city.send_keys('Smolensk')

            country = self.browser.find_element(By.ID, 'country')
            country.send_keys('Russia')

            submit = self.browser.find_element(By.CSS_SELECTOR, 'button.btn')
            submit.click()
        finally:
            time.sleep(30)
            self.browser.quit()

    def get_answer(self):
        self.open_link_by_text()
        self.fill_the_form()


if __name__ == '__main__':
    lesson = Lesson()
    lesson.get_answer()
