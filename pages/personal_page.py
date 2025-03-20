from pages.base_page import BasePage
from locators.personal_page_locators import PersonalPageLocators
import allure

class PersonalPage(BasePage):
    @allure.step('Переходим в раздел истории заказов')
    def click_order_history_button(self):
        self.click_element(PersonalPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Нажимаем кнопку выхода из аккаунта')
    def click_logout_button(self):
        self.click_element(PersonalPageLocators.LOGOUT_BUTTON)

    @allure.step('Проверяем открытие личного кабинета')
    def is_profile_page_opened(self):
        return self.get_current_url() == self.base_url + 'account'