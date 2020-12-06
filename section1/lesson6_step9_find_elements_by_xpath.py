from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Lesson:
    def __init__(self):
        self.url = 'http://suninjuly.github.io/find_xpath_form'

        self.browser = webdriver.Chrome()

    def get_answer(self):
        self.browser.get(self.url)
        try:
            first_name = self.browser.find_element(By.TAG_NAME, 'input')
            first_name.send_keys('Ivan')

            last_name = self.browser.find_element(By.NAME, 'last_name')
            last_name.send_keys('Petrov')

            city = self.browser.find_element(By.CLASS_NAME, 'city')
            city.send_keys('Smolensk')

            country = self.browser.find_element(By.ID, 'country')
            country.send_keys('Russia')

            submit = self.browser.find_element(By.XPATH, '//*[@type="submit"]')
            submit.click()
        finally:
            sleep(20)
            self.browser.quit()


if __name__ == '__main__':
    lesson = Lesson()
    lesson.get_answer()
