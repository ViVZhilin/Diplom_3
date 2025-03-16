from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:

    EMAIL_INPUT_FIELD = (By.XPATH, ".//label[contains(text(), 'Email')]")  # Блок отображения Email
    EMAIL_INPUT = (By.XPATH, ".//div[@class = 'input pr-6 pl-6 input_type_text input_size_default input_status_active']/input")  # Поле ввода Email
    RESET_PASSWORD = [By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"] #Кнопка "Восстановить"
    PASSWORD_INPUT_FIELD = (By.XPATH, ".//label[contains(text(), 'Пароль')]")
    PASSWORD_INPUT = (By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default']")
    HIDE_PASSWORD_BUTTON = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")