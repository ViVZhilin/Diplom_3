import allure
from pages.base_page import BasePage
from locators.order_list_page_locators import OrderListLocators

class OrderListPage(BasePage):

    @allure.step('Открываем детали заказа')
    def open_order_details(self):
        self.click_element(OrderListLocators.ORDER_LIST)

    @allure.step('Закрываем детали заказа')
    def close_order_details(self):
        # Ожидаем появления кнопки закрытия и кликаем по ней
        element = self.find_element_script(OrderListLocators.CLOSE_BUTTON_IN_MODAL)
        self.perform_action(element, "move_to_element")

    @allure.step('Получаем общее количество заказов')
    def get_total_order_amount(self):
        element = self.wait_for_element(OrderListLocators.TOTAL_ORDER_AMOUNT, timeout=10)
        return int(element.text)

    @allure.step('Получаем сегодняшнее количество заказов')
    def get_today_order_amount(self):
        return int(self.get_element_text(OrderListLocators.TODAY_ORDER_AMOUNT))

    @allure.step('Получаем значение заказа в работе')
    def is_order_in_work(self):
        order_element = self.wait_for_element(OrderListLocators.ORDER_IN_WORK, timeout=20)

        # Получаем текст элемента
        value = self.execute_script("return arguments[0].textContent;", order_element)

        # Убираем лишние пробелы и преобразуем в int
        order_id = int(value.strip())
        return order_id

    def test_modal_visibility(self):
        # Ожидание появления элемента с классом
        modal = self.find_element_script(OrderListLocators.MODAL_WINDOW_CONTAINER)

        # Получение значения свойства visibility
        return modal.value_of_css_property("visibility")