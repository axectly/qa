from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считываю значение x
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_tag_name("input[required]")
    input.send_keys(y)

    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radio = browser.find_element_by_css_selector("[value='robots']")
    radio.click()
    
    submit = browser.find_element_by_css_selector(".btn.btn-primary")
    submit.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта 
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
