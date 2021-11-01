from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'There is no "login" in url'       
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_INPUT), "Email input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_INPUT), "Password input is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL_INPUT), "Email registration input is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD1_INPUT), "Password for input registration  is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD2_INPUT), "Password confirm input registration is not presented"
        assert True