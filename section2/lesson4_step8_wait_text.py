import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Robot:
    def __init__(self):
        self.url = 'http://suninjuly.github.io/explicit_wait2.html'
        self.browser = webdriver.Chrome()
        self.x = None
        self.answer = None

    def _calculate_answer(self):
        self.answer = math.log(abs(12 * math.sin(int(self.x))))

    def _book_house(self):
        self.browser.get(self.url)
        WebDriverWait(self.browser, 12).until(ec.text_to_be_present_in_element((By.ID, 'price'), '$100'))
        self.browser.find_element_by_id('book').click()

    def _fill_form(self):
        self.x = self.browser.find_element_by_id('input_value').text
        self._calculate_answer()

        answer_field = self.browser.find_element_by_id('answer')
        answer_field.send_keys(f'{self.answer}')

        self.browser.find_element_by_id('solve').click()

    def run_test(self):
        try:
            self._book_house()
            self._fill_form()
        finally:
            time.sleep(10)
            self.browser.quit()


if __name__ == '__main__':
    robot = Robot()
    robot.run_test()
