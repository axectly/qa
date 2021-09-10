from selenium import webdriver
import time

link = "https://pgbonus.ru/"
email_old = "maul43@mail.ru"
email_new = "smoke-10-08@rambler.ru"
email_koleso = "smoke1-10-08@rambler.ru"
phone_new = "9016322185"
phone_koleso = "9178102589"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def login(browser):
        # переход на сайт
        browser.get(link)
        open_btn = browser.find_element_by_css_selector("div.newheader__topline-links a.link__login")
        open_btn.click()
        # заполнение данных для входа
        login_field = browser.find_element_by_css_selector("input#loginform-email")
        login_field.click()
        login_field.send_keys(email_old)
        password_field = browser.find_element_by_css_selector("input#password")
        password_field.click()
        password_field.send_keys("Qwerty10")
        captcha_field = browser.find_element_by_css_selector("input#loginform-captcha")
        captcha_field.click()
        time.sleep(5)
        # нажать на кнопку "ВОЙТИ"
        login_btn = browser.find_element_by_css_selector(".btn.btn-primary")
        login_btn.click()


    def assert_login(browser):
        # перейти на сайт
        browser.get(link)
        # вход в ЛК + проверка, что пользователь залогинен
        open_btn = browser.find_element_by_css_selector("div.newheader__topline-links a.link__login")
        open_btn.click()
        exit_btn = browser.find_element_by_css_selector(".button.mini.secondary")
        assert exit_btn.text == "ВЫЙТИ", "ОШИБКА: кнопка \"ВЫЙТИ\" не найдена"


    def assert_logout(browser):
        # выход из ЛК + проверка, что пользователь разлогинелся
        exit_btn = browser.find_element_by_css_selector(".button.mini.secondary")
        exit_btn.click()
        open_btn = browser.find_element_by_css_selector("div.newheader__topline-links a.link__login")
        assert open_btn.text == "  Вход", "ОШИБКА: кнопка \"Вход\" не найдена"


    def registration(browser, email, phone):
        # ввод данных для регистрации
        name_field = browser.find_element_by_css_selector("input#registrationform-first_name")
        name_field.click()
        name_field.send_keys("тестовыйаккаунтайсиэникс")
        email_field = browser.find_element_by_css_selector("input#registrationform-email")
        email_field.click()
        email_field.send_keys(email)
        phone_field = browser.find_element_by_css_selector("input#registrationform-phone")
        phone_field.click()
        phone_field.send_keys(phone)
        password_field = browser.find_element_by_css_selector("input#password")
        password_field.click()
        password_field.send_keys("Qwerty10")
        aggr_field = browser.find_element_by_css_selector("input#registrationform-aggr")
        aggr_field.click()
        # нажать на кнопку "ЗАРЕГИСТРИРОВАТСЬЯ"
        submit_btn = browser.find_element_by_css_selector("button.submit")
        submit_btn.click()

    def registration_koleso(browser, email, phone):
        # ввод данных для регистрации
        name_field = browser.find_element_by_css_selector("input#registrationform-first_name")
        name_field.click()
        name_field.send_keys("тестовыйаккаунтайсиэникс")
        email_field = browser.find_element_by_css_selector("input#registrationform-email")
        email_field.click()
        email_field.send_keys(email)
        phone_field = browser.find_element_by_css_selector("input#registrationform-phone")
        phone_field.click()
        phone_field.send_keys(phone)
        password_field = browser.find_element_by_css_selector("input#password")
        password_field.click()
        password_field.send_keys("Qwerty10")
        aggr_field = browser.find_element_by_css_selector("input#registrationform-aggr")
        aggr_field.click()
        # нажать на кнопку "ЗАРЕГИСТРИРОВАТСЬЯ"
        submit_btn = browser.find_element_by_css_selector("button.submit")
        submit_btn.click()


    def assert_new_user(browser):
        # проверка, что предупреждение о неподтверждённой почте присуствует
        alert = browser.find_element_by_css_selector("span>.confirmation.unconfirmed")
        assert alert.text == "ПОКА НЕ ПОДТВЕРЖДЕН", "ОШИБКА: текст \"Пока не подтвержден\" не найден"


    def assert_page(browser, btn_selector, page_url):
        browser.get(link)
        btn = browser.find_element_by_css_selector(btn_selector)
        btn.click()
        current_url = browser.current_url
        # print("Текущий url: " + current_url)
        # print("Ожидаемый url: " + page_url)
        assert current_url == page_url, "Переход на страницу не осуществлён"


    def pg_otzyv(browser):
        browser.get(link)
        original_handle = browser.current_window_handle
        otz_btn = browser.find_element_by_css_selector(".link__testimonials .menu__ico")
        otz_btn.click()
        title = browser.title
        assert title == "Призы за честные отзывы", "Тайтл страницы отличается от дефолтного"
        reg_btn = browser.find_element_by_css_selector(".site-button")
        reg_btn.click()
        assert browser.current_url == "https://pgbonus.ru/register?ptag=pg-otzyv", "Переход на страницу регистрации не осуществлён"
        browser.get(link)
        otz_btn = browser.find_element_by_css_selector(".link__testimonials .menu__ico")
        otz_btn.click()
        instr_btn = browser.find_element_by_class_name("site-intro__btn")
        assert instr_btn.text == "Инструкция для участников", "На странице отсутствует инструкция для участников"
        mail_text = browser.find_element_by_css_selector("[href='mailto:info@pgbonus.ru']")
        assert mail_text.text == "info@pgbonus.ru", "Адрес отправки писем указан неправильно"
        notific_btn = browser.find_element_by_css_selector(".notice-popup__close")
        notific_btn.click()
        rules_btn = browser.find_element_by_css_selector("[href = 'https://img.pgbonus.ru/projects/pg-otzyv/Rules.pdf']")
        rules_btn.click()
        for window_handle in browser.window_handles:
            if window_handle != original_handle:
                browser.switch_to.window(window_handle)
                break
        assert browser.current_url == "https://img.pgbonus.ru/projects/pg-otzyv/Rules.pdf", "Не осуществлён переход на страницу с правилами"
        browser.close()
        for window_handle in browser.window_handles:
            if window_handle == original_handle:
                browser.switch_to.window(window_handle)
                break
        raiting_btn = browser.find_element_by_css_selector("[href = 'https://img.pgbonus.ru/pgotzyv/rating.pdf']")
        raiting_btn.click()


    def pg_ended(browser):
        browser.get(link)
        ended_btn = browser.find_element_by_css_selector(".menu__link.link__ended")
        ended_btn.click()
        assert browser.current_url == "https://pgbonus.ru/promos/promo/ended", "Переход на страницу завершённых акций не осуществлён"
        reg_button = browser.find_element_by_css_selector(".scan-button")
        reg_button.click()
        assert browser.current_url == "https://pgbonus.ru/register?ptag=cashback&to_scan=true", "Переход на страницу регистрации не осуществлён"


    def pg_promos(browser):
        browser.get(link)
        title = browser.title
        assert title == "Специальные акции P&G", "Заголовок страницы \"https://pgbonus.ru/promos\" не соответствует оригиналу"
        pgbonus_btn = browser.find_element_by_css_selector(".main__link")
        pgbonus_btn.click()
        assert browser.current_url == "https://pgbonus.ru/", "Ссылка на логотипе не работает"
        slabovid_btn = browser.find_element_by_css_selector("a>img.menu__ico")
        slabovid_btn.click()
        slabovidNew_btn = browser.find_element_by_css_selector("div.newheader__topline-links>a.bvi-panel-close")
        slabovidNew_btn.click()
        help_btn = browser.find_element_by_css_selector("a.link__help>svg.menu__ico")
        help_btn.click()
        assert browser.current_url == "https://pgbonus.ru/help", "Переход на страницу \"Помощь\" не осуществлён"
        browser.get(link)
        login_btn = browser.find_element_by_css_selector("div.newheader__topline a.link__login>svg.menu__ico")
        login_btn.click()
        assert browser.current_url == "https://pgbonus.ru/auth", "Переход на страницу \"Логин\" не осуществлён"

    def pg_koleso(browser):
        browser.get(link)
        time.sleep(10)
        koleso_btn = browser.find_element_by_css_selector(".wheel-popup__button-link")
        koleso_btn.click()
        assert browser.current_url == "https://pgbonus.ru/register?utm_popup=kruti-koleso&ptag=kruti-koleso", "Переход на страницу регистрации не осуществлён"
        text = browser.find_element_by_css_selector("div.field p.center")
        assert text.text == "Обязательно дождитесь перехода на новую страницу с призом после нажатия на кнопку.", "Текст предупреждения о призе не совпадает"
        registration(browser, email_koleso, phone_koleso)
        time.sleep(15)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


"""
# проверка авторизация и выхода зарегистрированного пользователя
def test_tc1(browser):
    print("\nНачало тестового сценария №1")
    login(browser)
    assert_login(browser)
    assert_logout(browser)
    print("Конец тестового сценария №1")
"""

# проверка регистрации нового пользователя и предупреждения о неподтверждённой почте
def test_tc2(browser):
    print("\nНачало тестового сценария №2")
    # переход на сайт
    browser.get(link)
    # открыть регистрацию
    open_btn = browser.find_element_by_css_selector("[href='/register']")
    open_btn.click()
    registration(browser, email_new, phone_new)
    assert_login(browser)
    assert_new_user(browser)
    print("Конец тестового сценария №2")

# после ручного подтверждения почты проверка отсутствия предупреждения о неподтверждённой почте

"""
# проверка редиректа на cashback пользователя после авторизации
def test_tc3(browser):
    print("\nНачало тестового сценария №3")
    login(browser)
    # проверка редиректа и авторизации на cashback
    #close_btn = browser.find_element_by_class_name("modal-wrapper__close")
    #close_btn.click()
    balance_field = browser.find_element_by_css_selector("div.widget-col.balance.ng-star-inserted>div.widget-header")
    balance_text = balance_field.text
    assert balance_text == "Баланс счета", "Текст баланс счета не присутствует на странице"
    print("Конец тестового сценария №3")


# проверка возможности перехода авторизованного пользователя по вкладкам из меню сайта
def test_tc4(browser):
    print("\nНачало тестового сценария №4")
    login(browser)
    time.sleep(5)
    # проверка перехода на девчат
    browser.get(link)
    original_window = browser.current_window_handle
    devchat_btn = browser.find_element_by_css_selector("div.menu > a:nth-child(3)")
    devchat_btn.click()
    for window_hande in browser.window_handles:
        if window_hande != original_window:
            browser.switch_to.window(window_hande)
            break
    assert browser.current_url == "https://www.devchat.ru/", "Переход на сайт Девчат не осуществлён"
    browser.close()
    browser.switch_to.window(original_window)
    print("Переход на девчат осуществлён")
    # проверка перехода на cashback
    browser.get(link)
    original_window = browser.current_window_handle
    cashback_btn = browser.find_element_by_css_selector(".link__cashback .menu__ico")
    cashback_btn.click()
    for window_hande in browser.window_handles:
        if window_hande != original_window:
            browser.switch_to.window(window_hande)
            break
    time.sleep(2)
    assert browser.current_url == "https://cashback.pgbonus.ru/main?tab=all", "Переход на сайт Кэшбэк не осуществлён"
    browser.close()
    browser.switch_to.window(original_window)
    print("Переход на кэшбэк осуществлён")
    # проверка перехода в отзывы
    assert_page(browser, ".link__testimonials .menu__ico", "https://pgbonus.ru/promos/pg-otzyv")
    print("Переход в отзывы осуществлён")
    # проверка перехода в акции
    assert_page(browser, ".link__actions .menu__ico", "https://pgbonus.ru/#a")
    print("Переход в акции осуществлён")
    # проверка перехода в завершённые акции
    assert_page(browser, ".link__ended .menu__ico", "https://pgbonus.ru/promos/promo/ended")
    print("Переход в незавершённые акции осуществлён")
    # проверка перехода в опросы
    # assert_page(browser, ".link__surveys .menu__ico", "https://pgbonus.ru/surveys")
    # проверка перехода в брэнды
    assert_page(browser, ".link__brands .menu__ico", "https://pgbonus.ru/brands")
    print("Переход в брэнды осуществлён")
    # проверка перехода в статьи
    assert_page(browser, ".link__articles .menu__ico", "https://pgbonus.ru/statji")
    print("Переход в статьи осуществлён")
    # проверка перехода в помощь
    assert_page(browser, ".newheader__topline-links>.link__help", "https://pgbonus.ru/help")
    print("Переход в помощь осуществлён")
    print("Конец тестового сценария №4")


# проверка возможности перехода неавторизованного пользователя по вкладкам из меню сайта
def test_tc5(browser):
    print("\nНачало тестового сценария №5")
    # проверка перехода на девчат
    browser.get(link)
    original_window = browser.current_window_handle
    devchat_btn = browser.find_element_by_css_selector("div.menu > a:nth-child(3)")
    devchat_btn.click()
    for window_hande in browser.window_handles:
        if window_hande != original_window:
            browser.switch_to.window(window_hande)
            break
    assert browser.current_url == "https://www.devchat.ru/", "Переход на сайт Девчат не осуществлён"
    browser.close()
    browser.switch_to.window(original_window)
    print("Переход на девчат осуществлён")
    # проверка перехода на cashback
    browser.get(link)
    original_window = browser.current_window_handle
    cashback_btn = browser.find_element_by_css_selector(".link__cashback .menu__ico")
    cashback_btn.click()
    for window_hande in browser.window_handles:
        if window_hande != original_window:
            browser.switch_to.window(window_hande)
            break
    balance = browser.find_element_by_css_selector("div.widget.cols-2 > :nth-child(1) >div.widget-header")
    assert balance.text == "РЕГИСТРАЦИЯ", "Переход на сайт Кэшбэк не осуществлён"
    browser.close()
    browser.switch_to.window(original_window)
    print("Переход на кэшбэк осуществлён")
    # проверка перехода в отзывы
    assert_page(browser, ".link__testimonials .menu__ico", "https://pgbonus.ru/promos/pg-otzyv")
    print("Переход в отзывы осуществлён")
    # проверка перехода в акции
    assert_page(browser, ".link__actions .menu__ico", "https://pgbonus.ru/#a")
    print("Переход в акции осуществлён")
    # проверка перехода в завершённые акции
    assert_page(browser, ".link__ended .menu__ico", "https://pgbonus.ru/promos/promo/ended")
    print("Переход в незавершённые акции осуществлён")
    # проверка перехода в опросы
    # assert_page(browser, ".link__surveys .menu__ico", "https://pgbonus.ru/surveys")
    # проверка перехода в брэнды
    assert_page(browser, ".link__brands .menu__ico", "https://pgbonus.ru/brands")
    print("Переход в брэнды осуществлён")
    # проверка перехода в статьи
    assert_page(browser, ".link__articles .menu__ico", "https://pgbonus.ru/statji")
    print("Переход в статьи осуществлён")
    # проверка перехода в помощь
    assert_page(browser, ".newheader__topline-links>.link__help", "https://pgbonus.ru/help")
    print("Переход в помощь осуществлён")
    print("Конец тестового сценария №5")


def test_tc6(browser):
    print("\nНачало тестового сценария №6")
    pg_otzyv(browser)
    time.sleep(5)
    print("Конец тестового сценария №6")


def test_tc7(browser):
    print("\nНачало тестового сценария №7")
    pg_ended(browser)
    time.sleep(5)
    print("Конец тестового сценария №7")


def test_tc8(browser):
    print("\nНачало тестового сценария №8")
    pg_promos(browser)
    print("Конец тестового сценария №8")


def test_tc9(browser):
    print("\nНачало тестового сценария №9")
    pg_koleso(browser)
    print("Конец тестового сценария №9")
"""

