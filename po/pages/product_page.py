from .base_page import BasePage
from .locators import ProductLocators

class ProductPage(BasePage):
    # def add_product_to_basket(self):
    #     self.should_be_login_url()
    #     self.add_to_basket()
    #     self.should_be_message_about_adding()
    #     self.should_be_message_basket_total()

    def should_be_login_url(self):
        assert "?promo=offer" in self.browser.current_url, "There is no '?promo=offer' in url"
        assert True

    def add_to_basket(self):
        self.browser.find_element(*ProductLocators.ADD_PRODUCT_TO_BASKET).click()

    def should_be_message_about_adding(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*ProductLocators.MESSAGE_ABOUT_ADDING), (
            "Message about adding is not presented")
        # Затем получаем текст элементов для проверки
        product_name = self.browser.find_element(*ProductLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductLocators.MESSAGE_ABOUT_ADDING).text
        # Проверяем, что название товара присутствует в сообщении о добавлении
        # Это можно было бы сделать с помощью split() и сравнения строк,
        # Но не вижу необходимости усложнять код
        assert product_name in message, "No product name in the message"

    def should_be_message_basket_total(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        # Затем получаем текст элементов для проверки
        message_basket_total = self.browser.find_element(*ProductLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductLocators.PRODUCT_PRICE).text
        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price in message_basket_total, "No product price in the message"