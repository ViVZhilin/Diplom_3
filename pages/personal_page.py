from .base_page import BasePage
import allure
from locators.personal_page_locators import PersonalPageLocators

class PersonalPage(BasePage):

    @allure.step('Переходим в раздел истории заказов')
    def click_order_history_button(self):
        self.click_element(PersonalPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Нажимаем кнопку выхода из аккаунта')
    def click_logout_button(self):
        self.click_element(PersonalPageLocators.LOGOUT_BUTTON)

    @allure.step('Проверяем открытие личного кабинета')
    def is_profile_page_opened(self):
        return self.wait_for_element(PersonalPageLocators.CURRENT_PAGE).get_attribute("href") == self.base_url + 'account'