from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import allure

class LoginPage(BasePage):
    @allure.step('Кликаем на кнопку регистрации')
    def click_registration_button(self):
        self.click_element(LoginPageLocators.REGISTRATION_BUTTON)

    @allure.step('Кликаем на кнопку восстановления пароля')
    def click_password_recover_button(self):
        self.click_element(LoginPageLocators.PASSWORD_RECOVER_BUTTON)

    @allure.step('Кликаем на поле ввода Email')
    def click_on_email_field(self):
        self.click_element(LoginPageLocators.EMAIL_INPUT_ACTIVE)

    @allure.step('Вводим Email')
    def enter_email(self, email):
        self.send_keys_to_element(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step('Вводим пароль')
    def enter_password(self, password):
        self.send_keys_to_element(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step('Кликаем на кнопку входа')
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON_ON_LOGIN_PAGE)