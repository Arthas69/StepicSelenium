import pytest

from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxProfile


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help='Choose language: es, fr or another...')
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')


@pytest.fixture(scope='class')
def locale(request):
    language = request.config.getoption('language')
    return language


@pytest.fixture(scope='function')
def browser(request, locale):
    browser_name = request.config.getoption('browser_name')

    if browser_name == 'chrome':
        print('\nStart chrome browser...')
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': locale})
        browser = webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        print('\nStart firefox browser...')
        fp = FirefoxProfile()
        fp.set_preference("intl.accept_languages", locale)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('You need to choose language to test')
    yield browser
    browser.quit()
