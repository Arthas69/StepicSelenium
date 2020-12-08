# Есть другие варианты сделать то же самое, но в инете их полно, если что

import pytest

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxProfile

link = 'some_link'

@pytest.fixture(scope='function')
def browser_chrome():
    options = ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

@pytest.fixture(scope='function')
def browser_firefox():
    fp = FirefoxProfile()
    fp.set_preference('intl.accept_languages', 'es')
    browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    browser.quit()


# Для Chrome
class ChromeClass:

    def test_with_foreign_language_chrome(self, browser_chrome):
        browser_chrome.get(link)
        assert True


# Для Firefox
class FirefoxClass:

    def test_with_foreign_language_firefox(self, browser_firefox):
        browser_firefox.get(link)
        assert True
