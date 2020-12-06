from selenium import webdriver


browser = webdriver.Chrome()

browser.get("https://fake-shop.com/book1.html")

add_button = browser.find_element_by_css_selector('.add')  # Return exception NoSuchElementException if nothing found
add_button.click()

browser.get("https://fake-shop.com/book2.html")

add_button = browser.find_element_by_css_selector('.add')
add_button.click()

browser.get("https://fake-shop.com/basket.html")

goods = browser.find_elements_by_css_selector('.good')  # Return empty list if nothing found (!NO exception)
assert len(goods) == 2

