import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Robot:
    def __init__(self):
        self.url = 'http://suninjuly.github.io/selects1.html'
        self.browser = webdriver.Chrome()

    def do_the_trick(self):
        try:
            self.browser.get(self.url)
            value_1 = self.browser.find_element_by_id('num1').text
            value_2 = self.browser.find_element_by_id('num2').text
            print(value_1, value_2, type(value_1), type(value_2))
            result = eval(f'{value_1} + {value_2}')
            print(result)

            select = Select(self.browser.find_element_by_tag_name('select'))
            select.select_by_visible_text(f'{result}')

            submit = self.browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
            submit.click()

        finally:
            time.sleep(10)
            self.browser.quit()


if __name__ == '__main__':
    robot = Robot()
    robot.do_the_trick()
