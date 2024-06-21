from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators

# 1 - Проверка перехода по клику на «Конструктор»

class TestMesto:
    def test_transfer_to_account_by_constructor(self, login: WebDriver):
        driver = login

        # Поиск и клик по кнопке "Конструктор"
        driver.find_element(*Locators.MAIN_CONSTRUCTOR).click()
        title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_BURGERS)).text
        assert title == "Соберите бургер"


    # 2 - Проверка перехода по клику на логотип Stellar Burgers

    def test_transfer_to_account_by_logo(self, login: WebDriver):
        driver = login

        # Поиск и клик по логотипу "Stellar Burgers"
        driver.find_element(*Locators.MAIN_LOGO_BURGERS).click()
        title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_BURGERS)).text
        assert title == "Соберите бургер"