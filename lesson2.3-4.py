from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # жму кнопку
    browser.find_element_by_css_selector(".btn.btn-primary").click()

    # принимаем алерт
    browser.switch_to.alert.accept()

    # считываю значение x
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_tag_name("input[required]")
    input.send_keys(y)

    browser.find_element_by_css_selector(".btn.btn-primary").click()

    # выводим текст алерта
    print(browser.switch_to.alert.text)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
