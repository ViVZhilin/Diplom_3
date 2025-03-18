from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_list_page_locators import OrderListLocators
import allure

class MainPage(BasePage):
    @allure.step('Кликаем на кнопку личного кабинета')
    def click_personal_page_button(self):
        self.click_element(MainPageLocators.PERSONAL_PAGE)

    @allure.step('Открываем страницу заказов')
    def click_order_list_button(self):
        self.click_element(MainPageLocators.ORDER_LIST_PAGE)

    @allure.step('Открываем страницу конструктора')
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_PAGE)

    @allure.step('Нажимаем кнопку входа')
    def click_login_button(self):
        self.click_element(MainPageLocators.LOGIN_BUTTON_ON_MAIN_PAGE)

    @allure.step('Добавляем ингредиент')
    def add_ingredient_to_constructor(self):
        buns = self.wait_for_element(MainPageLocators.BUN_IN_LIST)
        add_ingredient = self.wait_for_element(MainPageLocators.ADDED_INGREDIENTS)
        action = ActionChains(self.driver)
        action.drag_and_drop(buns, add_ingredient).perform()

    @allure.step('Нажимаем кнопку заказа')
    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Получаем ID заказа')
    def get_order_id(self):

        self.wait_for_element_visible(OrderListLocators.LOADING_MODAL_WINDOW)
        # Ожидаем, пока оверлей станет невидимым

        self.wait_for_element_invisibility(OrderListLocators.LOADED_MODAL_WINDOW)

        # Ожидаем появления элемента с ID заказа
        order_id_element = self.wait_for_element(MainPageLocators.ORDER_ID)
        return order_id_element.text

    @allure.step('Закрываем модальное окно')
    def close_order_modal(self):
        # Ожидаем появления класса Modal_modal__P3_V5
        self.wait_for_element_visible(OrderListLocators.LOADING_MODAL_WINDOW)

        # Ожидаем, пока оверлей станет невидимым
        self.wait_for_element_invisibility(OrderListLocators.LOADED_MODAL_WINDOW)

        # Ожидаем появления кнопки закрытия модального окна
        self.wait_for_element(MainPageLocators.CLOSE_BUTTON_IN_MODAL_WINDOW)

        # Используем JavaScript для клика, если стандартный клик не работает
        self.click_element(MainPageLocators.CLOSE_BUTTON_IN_MODAL_WINDOW)