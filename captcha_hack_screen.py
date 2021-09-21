import pytesseract
import time
from selenium import webdriver


link_auth = "https://pgbonus.ru/auth"
browser = webdriver.Chrome()
browser.get(link_auth)
# Get link to captcha on the auth page
find_captcha = browser.find_element_by_css_selector('#loginform-captcha-image')
captcha_image = find_captcha.screenshot_as_png

with open('captcha_screen.png', "wb") as file:
        file.write(captcha_image)
print('Made screen')

img = 'captcha_screen.png'

custom_config = r"lang='eng'--oem 3 --psm 6 outputbase digits"
captcha_value = pytesseract.image_to_string(img, config=custom_config)
print('Captcha value is:', captcha_value)


if (len(captcha_value) < 5):
        # Find captcha block
        find_captcha = browser.find_element_by_css_selector('#loginform-captcha-image').click()
        time.sleep(1)
        # Make screen of captcha
        captcha_image = find_captcha.screenshot_as_png

        # Save screen to file
        with open('captcha_screen2.png', "wb") as file:
                file.write(captcha_image)
        print('[+]Made screen of captcha again')
        img2 = 'captcha_screen2.png'

        captcha_value = pytesseract.image_to_string(img2, config=custom_config)

captcha_input = browser.find_element_by_css_selector('#loginform-captcha')
captcha_input.clear()
captcha_input.send_keys(captcha_value)
