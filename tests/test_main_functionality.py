import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage

class TestMainFunctionality:
    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    @allure.title('Проверка перехода на страницу заказов')
    def test_redirect_to_order_list_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_list_button()
        assert driver.current_url == main_page.base_url + 'feed'

    @allure.title('Проверка перехода на страницу конструктора')
    def test_redirect_to_constructor_tab(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_constructor_button()
        assert driver.current_url == main_page.base_url