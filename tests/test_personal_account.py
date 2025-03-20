import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_page import PersonalPage
from data import Data

class TestPersonalAccount:
    @allure.title('Проверка открытия личного кабинета')
    def test_personal_account(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        personal_page = PersonalPage(driver)
        main_page.open()
        main_page.click_personal_page_button()
        login_page.click_on_email_field()
        login_page.enter_email(Data.VALID_EMAIL)
        login_page.enter_password(Data.VALID_PASSWORD)
        login_page.click_login_button()
        main_page.click_personal_page_button()
        assert personal_page.is_profile_page_opened()