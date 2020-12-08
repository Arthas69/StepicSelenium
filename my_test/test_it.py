import pytest
from time import sleep

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By


@pytest.fixture(scope='function')
def case_data():
    options = ChromeOptions()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


class TestLesson:
    def test_page_one(self, browser):
        url = 'http://suninjuly.github.io/registration1.html'
        browser.get(url)
        first_name = browser.find_element_by_css_selector('div.first_block .first')
        first_name.send_keys('Ivan')

        last_name = browser.find_element_by_css_selector('div.first_block .second')
        last_name.send_keys('Petrov')

        email = browser.find_element_by_css_selector('div.first_block .third')
        email.send_keys('name@example.com')

        submit = browser.find_element(By.XPATH, '//button[@type="submit"]')
        submit.click()

        sleep(1)

        welcome_text_element = browser.find_element_by_tag_name('h1')
        welcome_text = welcome_text_element.text

        assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_page_two(self, browser):
        url = 'http://suninjuly.github.io/registration2.html'
        browser.get(url)
        first_name = browser.find_element_by_css_selector('div.first_block .first')
        first_name.send_keys('Ivan')

        last_name = browser.find_element_by_css_selector('div.first_block .second')
        last_name.send_keys('Petrov')

        email = browser.find_element_by_css_selector('div.first_block .third')
        email.send_keys('name@example.com')

        submit = browser.find_element(By.XPATH, '//button[@type="submit"]')
        submit.click()

        sleep(1)

        welcome_text_element = browser.find_element_by_tag_name('h1')
        welcome_text = welcome_text_element.text

        assertEqual("Congratulations! You have successfully registered!", welcome_text)
        # self.assertRaises()
