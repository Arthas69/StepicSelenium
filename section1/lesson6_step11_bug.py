from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Lesson:
    def __init__(self, url):
        self.url = url
        self.browser = webdriver.Chrome()

    def run_test(self):
        try:
            self.browser.get(self.url)
            first_name = self.browser.find_element_by_css_selector('div.first_block .first')
            first_name.send_keys('Ivan')

            last_name = self.browser.find_element_by_css_selector('div.first_block .second')
            last_name.send_keys('Petrov')

            email = self.browser.find_element_by_css_selector('div.first_block .third')
            email.send_keys('name@example.com')

            submit = self.browser.find_element(By.XPATH, '//button[@type="submit"]')
            submit.click()

            sleep(1)

            welcome_text_element = self.browser.find_element_by_tag_name('h1')
            welcome_text = welcome_text_element.text

            assert "Congratulations! You have successfully registered!" == welcome_text
        # except (AssertionError, NoSuchElementException) as err:
        #     print(err)
        # else:
        #     print('No errors!')
        finally:
            sleep(5)
            self.browser.quit()


if __name__ == '__main__':
    lesson1 = Lesson('http://suninjuly.github.io/registration1.html')
    lesson1.run_test()
    lesson2 = Lesson('http://suninjuly.github.io/registration2.html')
    lesson2.run_test()
