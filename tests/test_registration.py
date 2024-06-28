from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from constants import Constants


class TestMesto:
    

    def test_registration_password(self, driver, gen_email: WebDriver):
        
        driver.find_element(*Locators.MAIN_LOGIN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))
        driver.find_element(*Locators.IN_REG_LINK).click()
       
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_PAGE))
        password = 'burger'
        driver.find_element(*Locators.REG_FIELD_PWD).send_keys(password)
        assert len(driver.find_element(*Locators.REG_FIELD_PWD).get_attribute('value')) >= 6   
    
    def test_registration_chek_name(self, driver, gen_email: WebDriver):

        driver.find_element(*Locators.MAIN_LOGIN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))
        driver.find_element(*Locators.IN_REG_LINK).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_PAGE))
        driver.find_element(*Locators.REG_FIELD_NAME).send_keys(Constants.NAME)
        driver.find_element(*Locators.REG_FIELD_EMAIL).send_keys(gen_email)
        driver.find_element(*Locators.REG_FIELD_PWD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.REG_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))
        driver.find_element(*Locators.IN_FIELD_EMAIL).send_keys(gen_email)
        driver.find_element(*Locators.IN_FIELD_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.IN_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_PERSONAL_AC)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_TITLE))
        assert not driver.find_element(*Locators.PERSONAL_NAME).get_attribute('value') == ""

    def test_registration_chek_login(self, driver, gen_email: WebDriver):
        
        driver.find_element(*Locators.MAIN_LOGIN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))
        driver.find_element(*Locators.IN_REG_LINK).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_PAGE))
        driver.find_element(*Locators.REG_FIELD_NAME).send_keys(Constants.NAME)
        driver.find_element(*Locators.REG_FIELD_EMAIL).send_keys(gen_email)
        driver.find_element(*Locators.REG_FIELD_PWD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.REG_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))
        driver.find_element(*Locators.IN_FIELD_EMAIL).send_keys(gen_email)
        driver.find_element(*Locators.IN_FIELD_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.IN_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_PERSONAL_AC)).click()
        login = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_FIELD_LOGIN))
        assert login.get_attribute('value') == gen_email
        