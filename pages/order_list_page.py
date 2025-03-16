import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from .base_page import BasePage
from locators.order_list_page_locators import OrderListLocators


class OrderListPage(BasePage):

    @allure.step('Открываем детали заказа')
    def open_order_details(self):
        self.click_element(OrderListLocators.ORDER_LIST)

    @allure.step('Закрываем детали заказа')
    def close_order_details(self):
        # Закрываем детали заказа
        close_button = self.driver.find_element(*OrderListLocators.CLOSE_BUTTON_IN_MODAL)
        actions = ActionChains(self.driver)
        actions.move_to_element(close_button).click().perform()

    @allure.step('Получаем общее количество заказов')
    def get_total_order_amount(self):
        element = self.wait_for_element(OrderListLocators.TOTAL_ORDER_AMOUNT, timeout=10)
        return int(element.text)

    @allure.step('Получаем сегодняшнее количество заказов')
    def get_today_order_amount(self):
        return int(self.get_element_text(OrderListLocators.TODAY_ORDER_AMOUNT))

    @allure.step('Получаем значение заказа в работе')
    def is_order_in_work(self):
        order_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderListLocators.ORDER_IN_WORK)
        )

        # Получаем текст элемента
        value = self.driver.execute_script("return arguments[0].textContent;", order_element)

        # Преобразуем текст в число
        order_id = int(value)  # Убираем лишние пробелы и преобразуем в int
        return order_id