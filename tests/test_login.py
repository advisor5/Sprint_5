from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from constants import Constants
from constants import Url


class TestMesto:


    def test_login_button_in(self, driver: WebDriver): 

        driver.find_element(*Locators.MAIN_LOGIN).click()
        
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))
        driver.find_element(*Locators.IN_FIELD_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.IN_FIELD_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.IN_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_PERSONAL_AC)).click()
        login = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_FIELD_LOGIN)).get_attribute('value')
        assert login == Constants.EMAIL

    def test_login_personal_ac(self, driver: WebDriver):

        driver.find_element(*Locators.MAIN_PERSONAL_AC).click()
        
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))
        driver.find_element(*Locators.IN_FIELD_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.IN_FIELD_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.IN_BUTTON).click()
        
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_PERSONAL_AC)).click()
        login = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_FIELD_LOGIN)).get_attribute('value')
        assert login == Constants.EMAIL

    def test_login_by_form_reg(self, driver: WebDriver):
 
        driver.find_element(*Locators.MAIN_PERSONAL_AC).click()
        driver.find_element(*Locators.IN_REG_LINK).click()
        
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_PAGE))
        driver.find_element(*Locators.REG_LOGIN_LINK).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))
        driver.find_element(*Locators.IN_FIELD_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.IN_FIELD_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.IN_BUTTON).click()
        
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_PERSONAL_AC)).click()
        login = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_FIELD_LOGIN)).get_attribute('value')
        assert login == Constants.EMAIL
    
    def test_login_by_recovery(self, driver: WebDriver):
        
        driver.find_element(*Locators.MAIN_PERSONAL_AC).click()
        driver.find_element(*Locators.IN_RECOVERY_LINK).click()
        driver.find_element(*Locators.REG_LOGIN_LINK).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))
        driver.find_element(*Locators.IN_FIELD_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.IN_FIELD_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.IN_BUTTON).click()
        
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_PERSONAL_AC)).click()
        login = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_FIELD_LOGIN)).get_attribute('value')
        assert login == Constants.EMAIL
