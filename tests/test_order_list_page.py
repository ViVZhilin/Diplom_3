import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_list_page import OrderListPage
from urls import Url
from data import Data

class TestOrderList:


    def test_order_list(self, driver):
        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)

        main_page.open()
        main_page.click_order_list_button()
        order_list_page.open_order_details()
        order_list_page.close_order_details()
        assert order_list_page.test_modal_visibility() == "hidden"

    @allure.title('Проверка увеличения значения счетчиков')
    def test_order_counter(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_list_page = OrderListPage(driver)

        # Вход в аккаунт
        main_page.open()
        main_page.click_personal_page_button()
        login_page.click_on_email_field()
        login_page.enter_email(Data.VALID_EMAIL)
        login_page.enter_password(Data.VALID_PASSWORD)
        login_page.click_login_button()

        # Переход на страницу ленты заказов
        main_page.click_order_list_button()

        total_amount = order_list_page.get_total_order_amount()
        today_amount = order_list_page.get_today_order_amount()

        # Создание нового заказа
        main_page.click_constructor_button()
        main_page.add_ingredient_to_constructor()
        main_page.click_order_button()
        main_page.get_order_id()
        main_page.close_order_modal()

        # Проверка счетчика заказов
        main_page.click_order_list_button()
        assert order_list_page.get_total_order_amount() == total_amount + 1
        assert order_list_page.get_today_order_amount() == today_amount + 1

    @allure.title('Проверка отображения заказа в работе')
    def test_order_in_work(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_list_page = OrderListPage(driver)

        # Вход в аккаунт
        main_page.open()
        main_page.click_personal_page_button()
        login_page.click_on_email_field()
        login_page.enter_email(Data.VALID_EMAIL)
        login_page.enter_password(Data.VALID_PASSWORD)
        login_page.click_login_button()

        # Создание нового заказа
        main_page.click_constructor_button()
        main_page.add_ingredient_to_constructor()
        main_page.click_order_button()
        order_id = main_page.get_order_id()
        main_page.close_order_modal()

        # Проверка заказа в работе
        main_page.click_order_list_button()
        assert order_list_page.is_order_in_work() == int(order_id)