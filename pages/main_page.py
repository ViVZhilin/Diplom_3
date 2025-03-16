import time
import allure
from selenium.webdriver import ActionChains
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step('Кликакем на кнопку личного кабинета')
    def click_personal_page_button(self):
        #Вариант для Google Chrome
        self.click_element(MainPageLocators.PERSONAL_PAGE)

        #Вариант для Mozila Firefox
        #element = self.wait_for_element(MainPageLocators.PERSONAL_PAGE)
        #self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Открываем страницу заказов')
    def click_order_list_button(self):
        #self.wait_for_element(MainPageLocators.ORDER_LIST_PAGE)
        self.click_element(MainPageLocators.ORDER_LIST_PAGE)

    @allure.step('Открываем страницу конструктора')
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_PAGE)

    @allure.step('Нажимаем кнопку входа')
    def click_login_button(self):
        self.click_element(MainPageLocators.LOGIN_BUTTON_ON_MAIN_PAGE)

    @allure.step('Добавляем ингредиент')
    def add_ingredient_to_constructor(self):
        # Ожидаем появления ингредиента (булки) в списке
        buns = self.wait_for_element(MainPageLocators.BUN_IN_LIST)

        # Ожидаем появления области для добавления ингредиентов
        add_ingredient = self.wait_for_element(MainPageLocators.ADDED_INGREDIENTS)

        # Используем ActionChains для перетаскивания ингредиента
        action = ActionChains(self.driver)
        action.drag_and_drop(buns, add_ingredient).perform()

    @allure.step('Нажимаем кнопку заказа')
    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Получаем ID заказа')
    def get_order_id(self):
        time.sleep(3)
        return self.get_element_text(MainPageLocators.ORDER_ID)

    @allure.step('Закрываем модальное окно')
    def close_order_modal(self):
        time.sleep(3)
        self.click_element(MainPageLocators.CLOSE_BUTTON_IN_MODAL_WINDOW)