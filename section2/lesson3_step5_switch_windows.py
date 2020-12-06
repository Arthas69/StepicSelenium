from selenium import webdriver

url = 'some'
browser = webdriver.Chrome()


browser.get(url)

new_window = browser.window_handles[1]    # Второе открытое окно
first_window = browser.window_handles[0]  # Запоминаем имя первого окна

browser.switch_to.window(new_window)
