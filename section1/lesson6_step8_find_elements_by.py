from random import choice
from string import ascii_lowercase
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Huge:
    def __init__(self):
        self.alpha = list(ascii_lowercase)
        self.url = 'http://suninjuly.github.io/huge_form.html'

        self.browser = webdriver.Chrome()

    def _fill_field(self):
        return [choice(self.alpha) for _ in range(5)]

    def get_answer(self):
        self.browser.get(self.url)
        try:
            elements = self.browser.find_elements_by_xpath('//*[@type="text"]')
            for element in elements:
                string = self._fill_field()
                element.send_keys(string)
            submit = self.browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
            submit.click()
        finally:
            sleep(5)
            self.browser.quit()


if __name__ == '__main__':
    huge_form = Huge()
    huge_form.get_answer()
