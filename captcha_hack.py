import pytesseract
import requests
from PIL.Image import Image
from selenium import webdriver


link_auth = "https://pgbonus.ru/auth"
browser = webdriver.Chrome()
browser.get(link_auth)

# Get link to captcha on the auth page
link_to_captcha = browser.find_element_by_css_selector(
    '#loginform-captcha-image')
captcha_url = link_to_captcha.get_attribute('src')

print(captcha_url)


def download_captcha_image():
    response = requests.get(captcha_full_link)
    img_bytes = response.content

    fname = 'captcha.png'
    with open(fname, 'wb') as f:
        f.write(img_bytes)
    
    img = Image.open(fname)
    return img
