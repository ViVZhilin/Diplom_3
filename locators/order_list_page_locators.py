from selenium.webdriver.common.by import By

class OrderListLocators:
    ORDER_MODAL_WINDOW = (By.XPATH, ".//div[@class = 'Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']")
    CLOSE_BUTTON_IN_MODAL = (By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    TOTAL_ORDER_AMOUNT = (By.XPATH, ".//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    TODAY_ORDER_AMOUNT = (By.XPATH, "//div[p[contains(@class, 'text_type_main-medium') and contains(text(), 'Выполнено за сегодня')]]/p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    ORDER_LIST = (By.CLASS_NAME, "OrderHistory_link__1iNby")
    ORDER_IN_WORK = (By.XPATH, "//li[@class='text text_type_digits-default mb-2']")
    MODAL_WINDOW_CONTAINER = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")
