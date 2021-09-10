import pytest
import time

from selenium import webdriver
from auth_data import login_email, password, link
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:

    browser = webdriver.Chrome()
    browser.get(link)
    
    
    def login(browser):
        # Open google chrome
        browser = webdriver.Chrome()
        # Go to link
        browser.get(link)
        # Click login button
        login_button = browser.find_element_by_css_selector('.link__login').click()

        # Clear and input email
        email_input = browser.find_element_by_css_selector('#loginform-email')
        email_input.clear()
        email_input.send_keys(login_email)

        # Clear and input password
        password_input = browser.find_element_by_css_selector('#password')
        password_input.clear()
        password_input.send_keys(password)






finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
