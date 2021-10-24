from selenium import webdriver

url = "http://selenium1py.pythonanywhere.com/"

class BasePage():
    def __init__(self, browser: webdriver, url):
        self.browser = browser
        self.url = url

    def open(self): 
        self.browser.get(self.url)