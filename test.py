import time

def test_tc1(browser):
    browser.get("https://pgbonus.ru")
    original_window = browser.current_window_handle
    devchat_btn = browser.find_element_by_css_selector(".menu__link.link__devchat")
    devchat_btn.click()
    time.sleep(5)
    for window_handle in browser.window_handles:
        if window_handle != original_window:
            browser.switch_to.window(window_handle)
            break
    browser.close()
    browser.switch_to.window(original_window)
    time.sleep(5)