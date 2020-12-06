import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Robot:
    def __init__(self):
        self.url = 'http://suninjuly.github.io/get_attribute.html'
        self.browser = webdriver.Chrome()
        self.x = None
        self.captcha_answer = None

    def calculate_answer(self):
        self.captcha_answer = str(math.log(abs(12 * math.sin(int(self.x)))))

    def do_the_trick(self):
        try:
            self.browser.get(self.url)
            self.x = self.browser.find_element_by_id('treasure').get_attribute('valuex')
            self.calculate_answer()

            input_field = self.browser.find_element_by_id('answer')
            input_field.send_keys(self.captcha_answer)
            time.sleep(1)
            self.browser.find_element_by_id('robotCheckbox').click()
            time.sleep(1)
            self.browser.find_element_by_id('robotsRule').click()
            time.sleep(1)

            submit = self.browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
            submit.click()

        finally:
            time.sleep(10)
            self.browser.quit()


if __name__ == '__main__':
    robot = Robot()
    robot.do_the_trick()
