from .pages.main_page import MainPage
from .pages.product_page import ProductPage

import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)
    page.open()
    page = ProductPage(browser, browser.current_url)
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    
