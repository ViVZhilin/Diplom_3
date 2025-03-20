from selenium.webdriver.common.by import By

class MainPageLocators:

    PERSONAL_PAGE = (By.LINK_TEXT, "Личный Кабинет") #Кнопка "Личный кабинет"
    CONSTRUCTOR_PAGE = (By.XPATH, "//p[contains(text(), 'Конструктор')]") #Кнопка "Конструктор"
    ORDER_LIST_PAGE = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]")  # Кнопка "Лента Заказов"
    NAME_INPUT = (By.XPATH, ".//input[@name = 'name']") #Поле ввода имени
    LOGIN_BUTTON = (By.LINK_TEXT, "Войти") #Кнопка "Войти"
    PERSONAL_EMAIL_DATA = (By.XPATH, ".//ul[@class = 'Profile_profileList__3vTor']/li[2]/div/div/input") #Поле отображения Email пользователя в личном кабинете
    PERSONAL_EMAIL_FIELD = (By.XPATH, ".//div[@class = 'input pr-6 pl-6 input_type_text input_size_default input_status_disabled']") #Поле с данными Email
    PASSWORD_ERROR_MESSAGE = (By.XPATH, "//form/fieldset[3]/div/p[@class = 'input__error text_type_main-default']") #Сообщение об ошибке при неверном пароле
    EMAIL_ERROR_MESSAGE = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']/p[@class = 'input__error text_type_main-default']") #Сообщение об ошибке при неверном Email
    LOGO = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']") #Логотип
    SOUS_TITLE_BLOCK = (By.XPATH, "//h2[text()='Соусы']") #Заголовок блока соусов в конструкторе
    FILLINGS_TITLE_BLOCK = (By.XPATH, "//h2[text()='Начинки']")#Заголовок блока начинок в конструкторе
    BUNS_TITLE_BLOCK = (By.XPATH, "//h2[text()='Булки']") #Заголовок блока булок в конструкторе
    SOUS_TITLE = (By.XPATH, "//div/span[text()='Соусы']/parent::div") #Заголовок раздела соусов
    FILLINGS_TITLE = (By.XPATH, "//div/span[text()='Начинки']/parent::div") #Заголовок раздела начинок в конструкторе
    BUNS_TITLE = (By.XPATH, "//div/span[text()='Булки']/parent::div") #Заголовок раздела булок в конструкторе
    LOGIN_BUTTON_ON_MAIN_PAGE = (By.XPATH, ".//div[@class = 'BurgerConstructor_basket__container__2fUl3 mt-10']/button") #Кнопка "Войти" на главной странице
    LOGIN_BUTTON_ON_REGISTRATION_PAGE = (By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") #Кнопка "Войти" на странице регистрации
    BUN_IN_LIST = (By.XPATH, ".//a[@class = 'BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']") #Булочка в списке
    NEW_BUN_IN_LIST = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6c']")
    ADDED_INGREDIENTS = (By.XPATH, ".//ul[@class = 'BurgerConstructor_basket__list__l9dp_']") #Собранный конструктор
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    CLOSE_BUTTON_IN_MODAL_WINDOW = (By.XPATH,".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    INGREDIENTS_AMOUNT = (By.XPATH, ".//p[@class='counter_counter__num__3nue1']")
    LOADED_MODAL_WINDOW = (By.XPATH, ".//div[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']")
    LOADING_MODAL_WINDOW = (By.CLASS_NAME, "Modal_modal__P3_V5")
    ORDER_ID = (By.XPATH, ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
