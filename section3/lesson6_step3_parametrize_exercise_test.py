import time
import math

import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


link = 'https://stepik.org/lesson/{}/step/1'
pages = ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905']


@pytest.fixture
def browser():
    options = ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(2)
    yield browser
    browser.quit()


class TestCases:

    @pytest.mark.parametrize('page', pages)
    def test_pages_for_alien_messages(self, browser, page):
        browser.get(link.format(page))
        element = WebDriverWait(browser, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, 'textarea.string-quiz__textarea'))
        )
        answer = math.log(int(time.time()))
        element.send_keys(f'{answer}')

        browser.find_element_by_class_name('submit-submission').click()

        result_text = browser.find_element_by_class_name('smart-hints__hint').text

        assert result_text == 'Correct!', result_text
