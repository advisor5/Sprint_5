from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from constants import Constants

# Проверка, перехода к разделу "Начинки":
class TestMesto:
    def test_transfer_to_account_by_constructor(self, driver: WebDriver):
        assert driver.current_url == Constants.URL_SITE  
        
        # Поиск и клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.MAIN_PERSONAL_AC).click()
        # Ожидание загрузки страницы авторизации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))

        # Заполнить поля: "Email", "Пароль", нажать кнопку "Войти"
        driver.find_element(*Locators.IN_FIELD_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.IN_FIELD_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.IN_BUTTON).click()

        # Ожидание авторизации и загрузки страницы конструктора заказов 
        title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_BURGERS)).text
        assert title == "Соберите бургер"
        
        driver.find_element(*Locators.MAIN_TAB_FILLING).click()
        title_filling = driver.find_element(*Locators.MAIN_TITLE_FILLING)
        driver.execute_script("arguments[0].scrollIntoView();", title_filling)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_TITLE_FILLING))
        assert title_filling.text == 'Начинки' 

        driver.find_element(*Locators.MAIN_TAB_SOUS).click()
        title_sous = driver.find_element(*Locators.MAIN_TITLE_SOUS)
        driver.execute_script("arguments[0].scrollIntoView();", title_sous)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_TITLE_SOUS))
        assert title_sous.text == 'Соусы' 

        driver.find_element(*Locators.MAIN_TAB_BUNS).click()
        title_buns = driver.find_element(*Locators.MAIN_TITLE_BUNS)
        driver.execute_script("arguments[0].scrollIntoView();",title_buns)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_TAB_BUNS))
        assert title_buns.text == 'Булки' 
