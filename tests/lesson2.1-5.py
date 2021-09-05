from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_tag_name('input[required]')
    input.send_keys(y)

    option1 = browser.find_element_by_css_selector("[value='robots']")
    option1.click()
    option2 = browser.find_element_by_css_selector('#robotCheckbox')
    option2.click()
    option3 = browser.find_element_by_css_selector('.btn.btn-default')
    option3.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта 
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    