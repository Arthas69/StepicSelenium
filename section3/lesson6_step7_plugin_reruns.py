# в командной строке --reruns n -> говорит сколько раз нужно сделать реран упавшего теста
# --tb=line -> для вывода результата для каждого теста только одной линией

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")


def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")
