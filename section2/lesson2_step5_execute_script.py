from selenium import webdriver


url = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()

browser.get(url)

button = browser.find_element_by_tag_name('button')
browser.execute_script('return arguments[0].scrollIntoView(true);', button)  # scroll until element become visible (result element in upper part of the screen)
browser.execute_script('window.scrollBy(0, 100);')  # scrolls screen for 100 px down


