# Запуск pytest -s -v -m smoke __name__
# Если заранее не зарегистрировать метки в корневой директории в pytest.ini будет выдавать предупреждение

# варианты запуска
# pytest -s -v -m "not smoke" test_fixture8.py   - все тесты которые не smoke
# pytest -s -v -m "smoke or regression" test_fixture8.py   - те тесты которые smoke И те которые regression
# pytest -s -v -m "smoke and win10" test_fixture81.py   - те тесты которые smoke и win10 вместе


import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")