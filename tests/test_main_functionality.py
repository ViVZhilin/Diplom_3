import pytest
import allure
from pages.main_page import MainPage
from urls import Url

class TestMainFunctionality:
    @allure.title('Проверка перехода на страницу заказов')
    def test_redirect_to_order_list_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_list_button()
        assert main_page.get_current_url() == Url.FEED_URL

    @allure.title('Проверка перехода на страницу конструктора')
    def test_redirect_to_constructor_tab(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_constructor_button()
        assert main_page.get_current_url() == Url.BASE_URL