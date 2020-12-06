import time
import math

from selenium import webdriver


class Robot:
    def __init__(self):
        self.url = 'http://suninjuly.github.io/redirect_accept.html'
        self.browser = webdriver.Chrome()
        self.x = None
        self.answer = None

    def _calculate_answer(self):
        self.answer = math.log(abs(12 * math.sin(self.x)))

    def run_test(self):
        try:
            self.browser.get(self.url)

            button = self.browser.find_element_by_class_name('trollface')
            button.click()

            new_page = self.browser.window_handles[1]
            self.browser.switch_to.window(new_page)

            self.x = int(self.browser.find_element_by_id('input_value').text)
            self._calculate_answer()

            answer_field = self.browser.find_element_by_id('answer')
            answer_field.send_keys(f'{self.answer}')

            self.browser.find_element_by_css_selector('button.btn').click()
        finally:
            time.sleep(10)
            self.browser.quit()


if __name__ == '__main__':
    robot = Robot()
    robot.run_test()
