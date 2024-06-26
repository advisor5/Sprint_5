from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from constants import Url


class TestMesto:


    def test_transfer_from_account_by_constructor(self, login: WebDriver):
        driver = login

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_PERSONAL_AC)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_TITLE))
        driver.find_element(*Locators.MAIN_CONSTRUCTOR).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_BURGERS))
        assert  driver.current_url == Url.HOST

    def test_transfer_from_account_by_logo(self, login: WebDriver):
        driver = login

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_PERSONAL_AC)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_TITLE))
        driver.find_element(*Locators.MAIN_LOGO_BURGERS).click()
        
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_BURGERS))
        assert  driver.current_url == Url.HOST