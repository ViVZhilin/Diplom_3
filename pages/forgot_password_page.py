from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
import allure

class ForgotPasswordPage(BasePage):

    @allure.step('Кликаем на поле ввода Email')
    def click_on_email_field(self):
        self.click_element(ForgotPasswordPageLocators.EMAIL_INPUT_FIELD)

    @allure.step('Вводим Email')
    def enter_email(self, email):
        self.send_keys_to_element(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step('Нажимаем кнопку восстановления пароля')
    def click_reset_password_button(self):
        self.click_element(ForgotPasswordPageLocators.RESET_PASSWORD)

    @allure.step('Вводим пароль')
    def enter_new_password(self, password):
        self.send_keys_to_element(ForgotPasswordPageLocators.PASSWORD_INPUT, password)

    @allure.step('Проверяем видимость пароля')
    def is_password_visible(self):
        return self.wait_for_element(ForgotPasswordPageLocators.PASSWORD_INPUT).get_attribute('type') == 'text'