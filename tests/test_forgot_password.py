import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.forgot_password_page import ForgotPasswordPage
from data import Data


class TestForgotPassword:
    @allure.title('Проверка восстановления пароля')
    def test_forgot_password(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        main_page.open()
        main_page.click_login_button()
        login_page.click_password_recover_button()
        forgot_password_page.click_on_email_field()
        forgot_password_page.enter_email(Data.VALID_EMAIL)
        forgot_password_page.click_reset_password_button()
        forgot_password_page.enter_new_password(Data.NEW_PASSWORD)
        assert forgot_password_page.is_password_visible()