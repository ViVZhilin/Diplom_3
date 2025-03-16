import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_page import PersonalPage

class TestPersonalAccount:
    @pytest.fixture(scope="function")
    def driver(self, request):
        browser = request.config.getoption("--browser")
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        else:
            raise pytest.UsageError("--browser should be chrome or firefox")
        yield driver
        driver.quit()

    @allure.title('Проверка открытия личного кабинета')
    def test_personal_account(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        personal_page = PersonalPage(driver)

        main_page.open()
        main_page.click_personal_page_button()
        login_page.click_on_email_field()
        login_page.enter_email("viktor_zhilin_17_000@yandex.ru")
        login_page.enter_password("123456")
        login_page.click_login_button()
        main_page.click_personal_page_button()
        assert personal_page.is_profile_page_opened()