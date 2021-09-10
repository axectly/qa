import pytesseract
import requests
import time
from PIL import Image
from selenium import webdriver


link_auth = "https://pgbonus.ru/auth"
browser = webdriver.Chrome()
browser.get(link_auth)
# Get link to captcha on the auth page
link_to_captcha = browser.find_element_by_css_selector('#loginform-captcha-image').click()
time.sleep(1)
link_to_captcha = browser.find_element_by_css_selector('#loginform-captcha-image')
captcha_url = link_to_captcha.get_attribute('src')

print(captcha_url)


def download_captcha_image():
    response = requests.get(captcha_url)
    img_bytes = response.content

    fname = 'captcha.png'
    with open(fname, "wb") as file:
        file.write(img_bytes)
    print('Downloaded')
    
    img = Image.open(fname)
    return img

img = download_captcha_image()
print(pytesseract.image_to_string(img, config='digits'))
