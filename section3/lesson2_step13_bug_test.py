import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By


class TestLesson(unittest.TestCase):
    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=options)

    def tearDown(self):
        self.browser.quit()

    def test_page_one(self):
        self.url = 'http://suninjuly.github.io/registration1.html'
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

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_page_two(self):
        self.url = 'http://suninjuly.github.io/registration2.html'
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

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        # self.assertRaises()


if __name__ == '__main__':
    unittest.main()
