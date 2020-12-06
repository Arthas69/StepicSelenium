import time
import math

from selenium import webdriver


class Robot:
    def __init__(self):
        self.url = 'http://suninjuly.github.io/alert_accept.html'
        self.browser = webdriver.Chrome()
        self.x = None
        self.answer = None

    def _calculate_answer(self):
        self.answer = math.log(abs(12 * math.sin(self.x)))

    def _pass_alert(self):
        self.browser.get(self.url)

        button = self.browser.find_element_by_tag_name('button')
        button.click()

        alert = self.browser.switch_to.alert
        alert.accept()

    def _fill_form(self):
        self.x = int(self.browser.find_element_by_id('input_value').text)
        self._calculate_answer()

        answer_field = self.browser.find_element_by_id('answer')
        answer_field.send_keys(f'{self.answer}')

        self.browser.find_element_by_css_selector('button.btn').click()

        time.sleep(10)

        self.browser.quit()

    def run_test(self):
        self._pass_alert()
        self._fill_form()


if __name__ == '__main__':
    robot = Robot()
    robot.run_test()
