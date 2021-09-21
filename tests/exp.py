from selenium import webdriver
import time
from random import choice
from string import digits

try:
    browser = webdriver.Chrome()
    link_main_page = 'https://pgbonus.ru'
    email = 'testicnx011@rambler.ru'


    def phone_generator():
        phone_gen = ''.join(choice(digits) for i in range(9))
        return(str(9)+str(phone_gen))

    def test_registartion():
        
        # Go to main page
        browser.get(link_main_page)
        browser.find_element_by_css_selector('.newheader__topline-links [href="/register"]').click()

        # Clear and input name
        name_input = browser.find_element_by_css_selector('input#registrationform-first_name')
        name_input.clear()
        name_input.send_keys('test')

        # Clear and input email
        email_input = browser.find_element_by_css_selector('input#registrationform-email')
        # email_input.clear()
        email_input.send_keys(email)

        # Clear and input phone
        phone_input = browser.find_element_by_css_selector('input#registrationform-phone')
        phone_input.clear()
        phone_input.send_keys(phone_generator())
        

    test_registartion()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
