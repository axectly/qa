from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    REG_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD1_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD2_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
