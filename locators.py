from selenium.webdriver.common.by import By


class Locators:

    
    # Главная страница "Stellar Burgers"
    MAIN_LOGIN =(By.XPATH, ".//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт"
    MAIN_PERSONAL_AC = (By.LINK_TEXT, "Личный Кабинет") # Кнопка "Личный кабинет"
    MAIN_CONSTRUCTOR = (By.LINK_TEXT, "Конструктор") # Кнопка "Конструктор"
    MAIN_BURGERS = (By.XPATH, ".//h1[text()='Соберите бургер']")# Секция конфигурации бургера 
    MAIN_LOGO_BURGERS = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Логотив "Стеллар Бургер"    
    MAIN_CURRENT_TAB = (By.XPATH, ".//div[contains(@class,'tab_tab_type_current')]") # Класс активного таба
    
    # Страница "Регистрация"
    REG_PAGE = (By.XPATH, ".//h2[text()='Регистрация']") # Страница Регистрации
    REG_FIELD_NAME = (By.XPATH, ".//fieldset[1]//input") # Поле "Имя" в форме регистрации
    REG_FIELD_EMAIL = (By.XPATH, ".//fieldset[2]//input") # Поле "Email" в форме регистрации
    REG_FIELD_PWD = (By.XPATH, ".//input[@type='password']") # Поле "Пароль" в форме регистрации
    REG_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    REG_LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']") # Ссылка в футтере на страницу Входа
    
    # Страница "Вход"
    IN_PAGE = (By.XPATH, ".//h2[text()='Вход']") # Заголовок "Вход" на странице входа
    IN_REG_LINK = (By.LINK_TEXT, 'Зарегистрироваться') # Ссылка на форму регистрации
    IN_RECOVERY_LINK = (By.LINK_TEXT, 'Восстановить пароль') # Ссылка на восстановление пароля
    IN_FIELD_EMAIL = (By.XPATH, ".//input[@name='name']") # Поле "Email" в форме входа
    IN_FIELD_PASSWORD = (By.NAME, 'Пароль') # Поле "Пароль" в форме входа
    IN_BUTTON = (By.XPATH, ".//button[text()='Войти']") # Кнопка "Войти" в форме входа

    # Страница "Личный кабинет"
    PERSONAL_TITLE = (By.XPATH, ".//a[text()='Профиль']") # Название "Профиль" в личном кабинете
    PERSONAL_NAME = (By.XPATH, ".//input[@name='Name']") # Поле, содержащее Имя в личном кабинете
    PERSONAL_FIELD_LOGIN = (By.XPATH, ".//input[contains(@value,'@')]") # Поле, содержащее email в личном кабинете
    PERSONAL_EXIT = (By.XPATH, ".//button[text()='Выход']") # Кнопка "Выйти" в личном кабинете
    
