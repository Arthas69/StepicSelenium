import pytest

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import NoSuchElementException


def test_exception_one():
    try:
        options = ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(options=options)
        browser.get('http://selenium1py.pythonanywhere.com/')

        # Если элемент БУДЕТ НАЙДЕН на странице, исключение не будет вызвано и тест упадет
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector('button.btn')
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()


def test_exception_two():
    try:
        options = ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(options=options)
        browser.get('http://selenium1py.pythonanywhere.com/')

        # Так как такой кнопки нет на странице исключение БУДЕТ вызвано, тест будет считаться успешным
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector('no-such-button.btn')
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()
