import pytest
from selenium import webdriver
from constants import Constants
from locators import Locators

# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


 
@pytest.fixture #(scope="session") УБРАТЬ
def driver():
    browser = webdriver.Chrome()
    browser.get(Constants.URL_SITE)
    yield browser

    browser.quit()

@pytest.fixture
def login(driver):
        assert driver.current_url == Constants.URL_SITE  
        # Поиск и клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.MAIN_PERSONAL_AC).click()
        # Явное ожидание загрузки страницы авторизации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))

        # Заполнить поля: "Email", "Пароль", нажать кнопку "Войти"
        driver.find_element(*Locators.IN_FIELD_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.IN_FIELD_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.IN_BUTTON).click()

        #Найти кнопку Личный кабинет и проверить логин  
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_PERSONAL_AC)).click()
        login = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_FIELD_LOGIN)).get_attribute('value')
        assert login == Constants.EMAIL

        return driver