# if  alert window

from selenium import webdriver

url = 'some url'
browser = webdriver.Chrome()

browser.get(url)

alert = browser.switch_to.alert  # находит alert
alert_text = alert.text  # получить текст alert
alert.accept()  # Жмет кнопку OK

# Если у модального окна есть два варианта взаимодействия (ОК и отмена)
confirm = browser.switch_to.alert
confirm.accept()   # OK
confirm.dismiss()  # Отмена


# Еще вариант с prompt
prompt = browser.switch_to.alert
prompt.send_keys("Answer")
prompt.accept()



