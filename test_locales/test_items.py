import time

import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestLanguage:

    # def test_find_button_on_espanol(self, browser):
    #     browser.get(link)
    #     element = WebDriverWait(browser, 10).until(
    #         ec.visibility_of_element_located((By.CSS_SELECTOR, 'button.btn-add-to-basket'))
    #     )
    #     element_text = element.text
    #
    #     assert element_text == 'Añadir al carrito', f"Should be 'Añadir al carrito' but actually got '{element_text}'"

    # @pytest.mark.xfail
    # @pytest.mark.skip
    # def test_find_button_on_francais(self, browser):
    #     browser.get(link)
    #     element = WebDriverWait(browser, 10).until(
    #         ec.visibility_of_element_located((By.CSS_SELECTOR, 'button.btn-add-to-basket'))
    #     )
    #     element_text = element.text
    #
    #     assert element_text == 'Ajouter au panier', f"Should be 'Ajouter au panier' but actually got '{element_text}'"

    def test_add_basket_button_exists(self, browser):
        browser.get(link)
        # time.sleep(10)
        element = WebDriverWait(browser, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, '#add_to_basket_form > button'))
        )
        test_attr = element.get_attribute('class')

        assert 'btn-add-to-basket' in test_attr, 'Not the needed button'
