from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.base_url = "https://stellarburgers.nomoreparties.site/"

    @allure.step('Открываем сайт')
    def open(self):
        self.driver.get(self.base_url)

    @allure.step('Ждем загрузки элемента')
    def wait_for_element(self, locator, timeout=10):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step('Кликаем')
    def click_element(self, locator):
        self.wait_for_element(locator).click()

    @allure.step('Заполняем поле ввода')
    def send_keys_to_element(self, locator, text):
        self.wait_for_element(locator).send_keys(text)

    @allure.step('Получаем текст элемента')
    def get_element_text(self, locator):
        return self.wait_for_element(locator).text

    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Выполняем JavaScript')
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @allure.step('Находим элемент')
    def find_element_script(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Выполняем действие с помощью ActionChains')
    def perform_action(self, element, action_type="click"):

        actions = ActionChains(self.driver)
        if action_type == "click":
            actions.move_to_element(element).click().perform()
        elif action_type == "move_to_element":
            actions.move_to_element(element).perform()

    @allure.step('Проверяем видимость элемента')
    def wait_for_element_visible(self, locator, timeout=10):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Проверяем скрытие элемента')
    def wait_for_element_invisibility(self, locator, timeout = 10):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator))