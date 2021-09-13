import pytest
import time
import pytesseract

from selenium import webdriver
from auth_data import login_email, password, link_main_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:

    browser = webdriver.Chrome()
    browser.get(link_main_page)
    
    class TestLogin():    
        def login(browser):
            # Open google chrome
            browser = webdriver.Chrome()
            # Go to link
            browser.get(link_main_page)
            # Click login button
            browser.find_element_by_css_selector('.link__login').click()

            # Clear and input email
            email_input = browser.find_element_by_css_selector('#loginform-email')
            email_input.clear()
            email_input.send_keys(login_email)

            # Clear and input password
            password_input = browser.find_element_by_css_selector('#password')
            password_input.clear()
            password_input.send_keys(password)

            # Find captcha block
            find_captcha = browser.find_element_by_css_selector('#loginform-captcha-image')
            # Make screen of captcha
            captcha_image = find_captcha.screenshot_as_png

            # Save screen to file
            with open('captcha_screen.png', "wb") as file:
                    file.write(captcha_image)
            print('[+]Made screen of captcha')
            img = 'captcha_screen.png'

            # Print value of captcha
            captcha_value = pytesseract.image_to_string(img, lang='eng')
            print('[+]Captcha value is', captcha_value)

            # Clear and input captcha
            captcha_input = browser.find_element_by_css_selector('#loginform-captcha')
            captcha_input.clear()
            captcha_input.send_keys(captcha_value)





        






finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
