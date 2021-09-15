from os import name
import time
import pytesseract
from selenium import webdriver
from auth_data import login_email, password, link_main_page

try:
    browser = webdriver.Chrome()


    def decoration_start(name):
        """ Function that decorates the beginning of the test
        
        """
        print(f'======================={name}_start=======================')
        

    def decoration_finish(name):
        """ Function that decorates the ending of the test
        
        """
        print(f'========================{name}_end========================')


    def phone_generator():
        """ Return a random phone number
            Generates 9 + 9 random digits
         """
        phone_gen = ''.join(choice(digits) for i in range(9))
        return(str(9) + str(phone_gen))


    def test_login():
        decoration_start(test_login.__name__)
        # Go to link
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
        captcha_value = pytesseract.image_to_string(img, lang='eng', config='tessedit_char_whitelist=0123456789')

        # while len(captcha_value) < 5:
        #     # Find captcha block
        #     find_captcha = browser.find_element_by_css_selector('#loginform-captcha-image').click()
        #     time.sleep(1)
        #     # Make screen of captcha
        #     captcha_image = find_captcha.screenshot_as_png

        #     # Save screen to file
        #     with open('captcha_screen.png', "wb") as file:
        #             file.write(captcha_image)
        #     print('[+]Made screen of captcha again')
        #     img = 'captcha_screen.png'

        #     captcha_value = pytesseract.image_to_string(img, lang='eng', config='tessedit_char_whitelist=0123456789')
        # else:

        # Print value of captcha
        print('[+]New captcha value is', captcha_value)

        # Clear and input captcha
        captcha_input = browser.find_element_by_css_selector('#loginform-captcha')
        captcha_input.clear()
        captcha_input.send_keys(captcha_value)

        # Click auth button
        browser.find_element_by_css_selector('.btn.btn-primary').click()

        # Find message about success auth
        time.sleep(1)
        success_auth = browser.find_element_by_css_selector('.blue.center').text
        index = success_auth.find('входа')
        if index != -1:
            print(f'[+] Авторизация выполнена')
        else:
            print(f'Что-то пошло не так')
        decoration_finish(test_login.__name__)


    def test_logout():
        decoration_start(test_logout.__name__)
        # Go to main page
        browser.get(link_main_page)
        # Find LK button
        browser.find_element_by_css_selector('.newheader__topline-links [href="/lk"]').click()
        browser.find_element_by_css_selector('.button.mini.secondary').click()
        login_button = browser.find_element_by_css_selector('.newheader__topline-links [href="/auth"]').text
        index = login_button.find('Вход')
        if index != -1:
            print(f'[+] Логаут выполнен')
        else:
            print(f'Что-то пошло не так')
        decoration_finish(test_logout.__name__)


    def test_registartion():
        decoration_start(test_logout.__name__)
        
        # Go to main page
        browser.get(link_main_page)
        browser.find_element_by_css_selector('.newheader__topline-links [href="/register"]').click()

        # Input name
        name_input = browser.find_element_by_css_selector('input#registrationform-first_name')
        name_input.clear()
        name_input.send_keys('test')

        # Input email
        email_input = browser.find_element_by_css_selector('input#registrationform-email')
        email_input.clear()
        email_input.send_keys('testicnx011@rambler.ru')

        # Input random phone
        phone_input = browser.find_element_by_css_selector('input#registrationform-email')
        phone_input.clear()
        phone_input.send_keys(phone_generator())

        # Input password
        password_input = browser.find_element_by_css_selector('input#password')
        password_input.clear()
        password_input.send_keys(password)

        # ===добавить проверку на попытку реги без галочки===
    
        # Check agreement
        browser.find_element_by_css_selector('input#registrationform-aggr').click()

        # Click "Зарегистрироваться"
        


        decoration_finish(test_logout.__name__)


    def navigation():
        pass


    def blabla():
        pass

    test_login()
    test_logout()
    len()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()