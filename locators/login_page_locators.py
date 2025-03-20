from selenium.webdriver.common.by import By

class LoginPageLocators:

    REGISTRATION_BUTTON = (By.LINK_TEXT, "Зарегистрироваться")  # Кнопка "Зарегистрироваться"
    PASSWORD_RECOVER_BUTTON = (By.LINK_TEXT, "Восстановить пароль")  # Кнопка "Восстановить пароль"
    EMAIL_INPUT_ACTIVE = (By.XPATH, ".//label[contains(text(), 'Email')]")  # Блок отображения Email
    EMAIL_INPUT = (By.XPATH, ".//div[@class = 'input pr-6 pl-6 input_type_text input_size_default input_status_active']/input")  # Поле ввода Email
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля
    LOGIN_BUTTON_ON_LOGIN_PAGE = (By.XPATH, ".//form[@class = 'Auth_form__3qKeq mb-20']/button")  # Кнопка "Войти" на странице логина