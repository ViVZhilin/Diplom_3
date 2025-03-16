from selenium.webdriver.common.by import By

class PersonalPageLocators:
    EMAIL_FIELD = (By.XPATH, ".//label[contains(text(), 'Email')]") #Значение поля Email пользователя в личном кабинете
    ORDER_HISTORY_BUTTON = (By.LINK_TEXT, "История заказов")
    CURRENT_PAGE = (By.CSS_SELECTOR, "a[aria-current='page']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")