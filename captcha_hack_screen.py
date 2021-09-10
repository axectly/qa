import pytesseract
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

print(pytesseract.image_to_string(img, config='digits'))
