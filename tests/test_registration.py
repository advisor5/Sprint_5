from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random

from locators import Locators
from constants import Constants

class TestMesto:
    def test_registration(self, driver: WebDriver):
        assert driver.current_url == Constants.URL_SITE

        # Поиск и клик по кнопке "Войти в аккаунт"
        driver.find_element(*Locators.MAIN_LOGIN).click()
        # Ожидание загрузки страницы авторизации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))
        
        # Поиск и клик по ссылке "Зарегистрироваться"
        driver.find_element(*Locators.IN_REG_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_PAGE))
        assert driver.current_url == Constants.URL_REG

        # Найди поле "Имя" и заполни его
        # WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_PAGE))
        # assert driver.find_element(*Locators.REG_PAGE).text == 'Регистрация'
        name = "Sergei"
        driver.find_element(*Locators.REG_FIELD_NAME).send_keys(name)
        assert not driver.find_element(*Locators.REG_FIELD_NAME).get_attribute('value') == ""
        
        # Найди поле "Email" и заполни его
        email =  f"sergei_kravchuk10{random.randint(100, 999)}@ya.ru"
        driver.find_element(*Locators.REG_FIELD_EMAIL).send_keys(email)
        assert driver.find_element(*Locators.REG_FIELD_EMAIL).get_attribute('value') == email # ПРОВЕРКУ НА МАСКУ ЕМАИЛ
        
        # Найди поле "Пароль" и заполни его
        password = 'burger!'
        driver.find_element(*Locators.REG_FIELD_PWD).send_keys(password)
        assert len(driver.find_element(*Locators.REG_FIELD_PWD).get_attribute('value')) >= 6 # type: ignore ПОДУМАТЬ ОСТАВИТЬ ТАК
      
        # Найди кнопку "Зарегистрироваться" и кликни по ней
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.IN_PAGE))
        assert driver.current_url == Constants.URL_LOGIN

        # Ожидание загрузки страницы авторизации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))
        assert driver.find_element(*Locators.IN_PAGE).text == 'Вход'

        # Ввести в поле "Email" логин ПОПРОБОВАТЬ СОБРАТЬ В ОДИН БЛОК
        # driver.find_element(*Locators.IN_FIELD_EMAIL).clear() # ВРОДЕ ПОЧИНИЛ, ПРОВЕРИТЬ
        driver.find_element(*Locators.IN_FIELD_EMAIL).send_keys(email)
        assert driver.find_element(*Locators.IN_FIELD_EMAIL).get_attribute('value') == email
        
        # Ввести в поле "Пароль" пароль
        driver.find_element(*Locators.IN_FIELD_PASSWORD).send_keys(password)
        assert driver.find_element(*Locators.IN_FIELD_PASSWORD).get_attribute('value') == password
        # Нажать кнопку "Войти"
        driver.find_element(*Locators.IN_BUTTON).click()

        #Найти кнопку Личный кабинет и проверить логин  
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_PERSONAL_AC)).click()
        login = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_FIELD_LOGIN)).get_attribute('value')
        assert login == email
        

        

