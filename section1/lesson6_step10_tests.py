from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Lesson:
    def __init__(self):
        self.url = 'http://suninjuly.github.io/registration2.html'

        self.browser = webdriver.Chrome()

    def get_answer(self):
        self.browser.get(self.url)
        try:
            elements = self.browser.find_elements_by_tag_name('input')
            for element in elements:
                req = element.get_attribute('required')
                if req:
                    string = "text"
                    element.send_keys(string)

            submit = self.browser.find_element(By.CSS_SELECTOR, 'button.btn')
            submit.click()

            sleep(1)

            welcome_text_element = self.browser.find_element_by_tag_name('h1')
            welcome_text = welcome_text_element.text

            assert "Congratulations! You have successfully registered!" == welcome_text
        finally:
            sleep(20)
            self.browser.quit()


if __name__ == '__main__':
    lesson = Lesson()
    lesson.get_answer()
