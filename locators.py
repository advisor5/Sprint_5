from selenium.webdriver.common.by import By

class Locators:
    
    # Главная страница "Stellar Burgers"
    MAIN_LOGIN =(By.XPATH, ".//section/div/button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт"
    MAIN_PERSONAL_AC = (By.LINK_TEXT, "Личный Кабинет") # Кнопка "Личный кабинет"
    MAIN_CONSTRUCTOR = (By.LINK_TEXT, 'Конструктор') # Кнопка "Конструктор"
    MAIN_BURGERS = (By.XPATH,'.//section[1]/h1')# Секция конфигурации бургера 
    MAIN_LOGO_BURGERS = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2') # Логотив "Стеллар Бургер"
    MAIN_TAB_FILLING  = (By.XPATH, ".//span[text()='Начинки']") # Таб "Начинки" в конструкторе заказов
    MAIN_TITLE_FILLING = By.XPATH, ".//h2[3]" # Заголовок "Начинки" в конструкторе заказов
    MAIN_TAB_SOUS  = (By.XPATH, ".//span[text()='Соусы']") # Таб "Соусы" в конструкторе заказов
    MAIN_TITLE_SOUS = By.XPATH, ".//h2[2]" # Заголовок "Соусы" в конструкторе заказов
    MAIN_TAB_BUNS  = (By.XPATH, ".//span[text()='Булки']") # Таб "Булки" в конструкторе заказов
    MAIN_TITLE_BUNS = By.XPATH, ".//div[2]/h2[1]" # Заголовок "Булки" в конструкторе заказов

    # Страница "Регистрация"
    REG_PAGE = (By.XPATH, ".//div[@class='Auth_login__3hAey']/h2[text()='Регистрация']") # Страница Регистрации
    REG_FIELD_NAME = (By.XPATH, ".//fieldset[1]//div/input") # Поле "Имя" в форме регистрации
    REG_FIELD_EMAIL = (By.XPATH, ".//fieldset[2]//div/input") # Поле "Email" в форме регистрации
    REG_FIELD_PWD = (By.XPATH, ".//input[@type='password']") # Поле "Пароль" в форме регистрации
    REG_BUTTON = (By.XPATH, "//*[@id='root']/div/main/div/form/button") # Кнопка "Зарегистрироваться"
    REG_LOGIN_LINK = (By.CLASS_NAME, "Auth_link__1fOlj") # Ссылка в футтере на страницу Входа
    
    # Страница "Вход"
    IN_PAGE = (By.XPATH, ".//div[@class='Auth_login__3hAey']/h2[text()='Вход']") # Страница Входа
    IN_REG_LINK = (By.LINK_TEXT, 'Зарегистрироваться') # Ссылка на форму регистрации
    IN_RECOVERY_LINK = (By.LINK_TEXT, 'Восстановить пароль') # Ссылка на восстановление пароля
    IN_FIELD_EMAIL = (By.XPATH, './/fieldset[1]//div/input') # Поле "Email" в форме входа
    IN_FIELD_PASSWORD = (By.NAME, 'Пароль') # Поле "Пароль" в форме входа
    IN_BUTTON = (By.XPATH, ".//form/button") # Кнопка "Войти" в форме входа

    # Страница "Личный кабинет"
    PERSONAL_FIELD_LOGIN = (By.XPATH, ".//li[2]/div/div/input") # Поле, содержащее Логин в личном кабинете
    PERSONAL_EXIT = (By.XPATH, ".//ul/li[3]/button") # Кнопка "Выйти в личном кабинете"
    PERSONAL_TITLE = (By.XPATH, ".//main//li[1]/a") # Название "Профиль" в личном кабинете
