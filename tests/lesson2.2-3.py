from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# считаю сумму а + б
def sum(a, b):
    return str(a + b)  # сразу перевожу значение в строку


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считываю значение в поле1
    a_element = browser.find_element_by_css_selector("#num1")
    a = a_element.text

    # считываю значение в поле1
    b_element = browser.find_element_by_css_selector("#num2")
    b = b_element.text

    # перевожу строковое значение а и b в integer, чтобы посчитать
    y = sum(int(a), int(b))

    # раскрываю выпадающий список
    select = Select(browser.find_element_by_tag_name("select"))

    # выбираю значение из списка, равное моей сумме из 7й строки
    select.select_by_value(y)
    browser.find_element_by_css_selector(".btn.btn-default").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
