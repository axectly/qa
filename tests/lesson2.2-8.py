from selenium import webdriver
import time
import os

#указываем какой и откуда брать файл 
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "test.txt"
file_path = os.path.join(current_dir, file_name)
    
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('[name="firstname"]').send_keys('Leo')
    browser.find_element_by_css_selector('[name="lastname"]').send_keys('Messi')
    browser.find_element_by_css_selector('[name="email"]').send_keys('psg@fc.com')
   
    element = browser.find_element_by_css_selector("[type='file']")
    element.send_keys(file_path)

    browser.find_element_by_css_selector(".btn.btn-primary").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
