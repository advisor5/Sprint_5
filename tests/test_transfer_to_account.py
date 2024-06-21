from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from constants import Constants

# Проверка перехода по клику на «Личный кабинет»

class TestMesto:
    def test_transfer_to_accaunt(self, driver: WebDriver):
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

        #Найти кнопку Личный кабинет и войти 
        # WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_TITLE))
        # assert driver.find_element(*Locators.PERSONAL_FIELD_LOGIN).get_attribute('value') == Constants.EMAIL

        