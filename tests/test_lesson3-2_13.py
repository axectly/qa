import unittest
from selenium import webdriver
import time

welc = "Congratulations! You have successfully registered!"
def registration(link):
    with webdriver.Chrome() as browser:
        browser.get(link)

        input1 = browser.find_element_by_css_selector('.first_block .first')
        input1.send_keys("Iva n")
        input2 = browser.find_element_by_css_selector('.first_block .second')
        input2.send_keys("P etrov")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("Pet rov")
        time.sleep(1)

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        return welcome_text_elt.text

class TestsForPages(unittest.TestCase):
    def test_first_page(self):
        p1 = registration("http://suninjuly.github.io/registration1.html")
        self.assertEqual(p1, welc)

    def test_second_page(self):
        p2 = registration("http://suninjuly.github.io/registration2.html")
        self.assertEqual(p2, welc)


if __name__ == "__main__":
    unittest.main()