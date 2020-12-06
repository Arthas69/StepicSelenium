from selenium import webdriver
from selenium.webdriver.support.ui import Select

# example
url = 'http://suninjuly.github.io/selects2.html'
browser = webdriver.Chrome()

browser.get(url)

select = Select(browser.find_element_by_tag_name('select'))
# С методом select_by_* не нужно применять click() для выбора
value = select.select_by_value('1')  # значение атрибута value
text = select.select_by_visible_text('Python')  # текст записаны в тэг option
index = select.select_by_index('1')  # порядковый номер в списке (индексация начинается с 0)

browser.quit()
