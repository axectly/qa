import time
import pytesseract
from random import choice
from string import digits
from selenium import webdriver
from auth_data import login_email, password, link_main_page

browser = webdriver.Chrome()

def test_login(browser):
    browser.get(link_main_page)
    

    # Click login button
    browser.find_element_by_css_selector('.newheader__topline-links [href="/auth"]').click()

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
    captcha_value = pytesseract.image_to_string(img, lang='eng', config='-c tessedit_char_whitelist=0123456789')
    print('Captcha value is:', captcha_value)
    # удаляем 2 посл. символа т.к. 
    captcha_value = captcha_value[:-2]
    print(len(captcha_value))
    while (len(captcha_value) < 5):
        print('gg')
        # Find captcha block
        find_captcha.click()
        time.sleep(1)
        # Make screen of captcha
        captcha_image = find_captcha.screenshot_as_png

        # Save screen to file
        with open('captcha_screen2.png', "wb") as file:
                file.write(captcha_image)
        print('[+]Made screen of captcha again')
        img2 = 'captcha_screen2.png'

        captcha_value = pytesseract.image_to_string(img2, lang='eng', config='-c tessedit_char_whitelist=0123456789')
    else:
        # Print value of captcha
        print('[+]New captcha value is', captcha_value)

    # Clear and input captcha
    captcha_input = browser.find_element_by_css_selector('#loginform-captcha')
    captcha_input.clear()
    captcha_input.send_keys(captcha_value)

test_login(browser)