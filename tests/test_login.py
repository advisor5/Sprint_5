from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from constants import Constants


class TestMesto:
    # @pytest.mark.usefixture('driver') # почитать 

    # 1 - Проверка входа по кнопке "Войти в аккаунт" на главной

    def test_login_button_in(self, driver: WebDriver):
        assert driver.current_url == Constants.URL_SITE  

        # Поиск и клик по кнопке "Войти в аккаунт"
        driver.find_element(*Locators.MAIN_LOGIN).click()
        # Ожидание загрузки страницы авторизации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))

        # Заполнить поля: "Email", "Пароль", нажать кнопку "Войти"
        driver.find_element(*Locators.IN_FIELD_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.IN_FIELD_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.IN_BUTTON).click()

        #Найти кнопку Личный кабинет и проверить логин  
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_PERSONAL_AC)).click()
        login = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_FIELD_LOGIN)).get_attribute('value')
        assert login == Constants.EMAIL

    # 2 - Проверка входа через кнопку "Личный кабинет"

    def test_login_personal_ac(self, driver: WebDriver):
        assert driver.current_url == Constants.URL_SITE  

        # Поиск и клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.MAIN_PERSONAL_AC).click()
        # Ожидание загрузки страницы авторизации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))

        # Заполнить поля: "Email", "Пароль", нажать кнопку "Войти"
        driver.find_element(*Locators.IN_FIELD_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.IN_FIELD_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.IN_BUTTON).click()
        
        #Найти кнопку Личный кабинет и проверить логин  
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_PERSONAL_AC)).click()
        login = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_FIELD_LOGIN)).get_attribute('value')
        assert login == Constants.EMAIL


    # 3 - Проверка входа через кнопку в форме регистрации

    def test_login_by_form(self, driver: WebDriver):
        assert driver.current_url == Constants.URL_SITE
 
        # Поиск и клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.MAIN_PERSONAL_AC).click()
        
        # Поиск и клик по ссылке "Зарегистрироваться"
        driver.find_element(*Locators.IN_REG_LINK).click()
        # Ожидание загрузки страницы регистрации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_PAGE))

        # Поиск и клик по тексту "Войти"
        driver.find_element(*Locators.REG_LOGIN_LINK).click()
        # Ожидание загрузки страницы авторизации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))
        
        # Заполнить поля: "Email", "Пароль", нажать кнопку "Войти"
        driver.find_element(*Locators.IN_FIELD_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.IN_FIELD_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.IN_BUTTON).click()
        
        #Найти кнопку Личный кабинет и проверить логин  
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_PERSONAL_AC)).click()
        login = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_FIELD_LOGIN)).get_attribute('value')
        assert login == Constants.EMAIL


    # 4 - Проверка входа через кнопку в форме восстановления пароля
    
    def test_login_by_recovery(self, driver: WebDriver):
        assert driver.current_url == Constants.URL_SITE
        # Поиск и клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.MAIN_PERSONAL_AC).click()

        # Поиск и клик по тексту "Восстановить пароль"
        driver.find_element(*Locators.IN_RECOVERY_LINK).click()
        # Поиск и клик по тексту "Войти"
        driver.find_element(*Locators.REG_LOGIN_LINK).click()
        # Ожидание загрузки страницы авторизации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))

        # Заполнить поля: "Email", "Пароль", нажать кнопку "Войти"
        driver.find_element(*Locators.IN_FIELD_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.IN_FIELD_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.IN_BUTTON).click()
        
        #Найти кнопку Личный кабинет и проверить логин  
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_PERSONAL_AC)).click()
        login = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_FIELD_LOGIN)).get_attribute('value')
        assert login == Constants.EMAIL
