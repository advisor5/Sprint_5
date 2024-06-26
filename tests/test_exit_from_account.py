from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from constants import Url

class TestMesto:


    def test_exit_from_account(self, login: WebDriver):
        driver = login

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_PERSONAL_AC)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_EXIT)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))
        assert driver.current_url == Url.URL_LOGIN
