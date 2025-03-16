from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site/"

    @allure.step('Открываем сайт')
    def open(self):
        self.driver.get(self.base_url)

    @allure.step('Ждем загрузки элемента')
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step('Кликаем')
    def click_element(self, locator):
        self.wait_for_element(locator).click()

    @allure.step('Заполняем поле ввода')
    def send_keys_to_element(self, locator, text):
        self.wait_for_element(locator).send_keys(text)

    @allure.step('Получаем текст элемента')
    def get_element_text(self, locator):
        return self.wait_for_element(locator).text