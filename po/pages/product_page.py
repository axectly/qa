from .base_page import BasePage
from .locators import ProductLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_login_url()
        self.add_to_basket()

    def should_be_login_url(self):
        assert "newYear2019" in self.browser.current_url, 'There is no "newYear2019" in url'       
        assert True

    def add_to_basket(self):
        self.browser.find_element(*ProductLocators.ADD_PRODUCT_TO_BASKET).click()