import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locators


class TestMesto:
    @pytest.mark.parametrize('name_section', ['Булки', 'Начинки', 'Соусы'])
    def test_transfer_between_sections(self, name_section, login: WebDriver):
        driver = login
        
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_BURGERS))
        element = driver.find_element(By.XPATH, f".//span[text()='{name_section}']")
        driver.execute_script("arguments[0].click();", element)
        
        activated_class = driver.find_element(*Locators.MAIN_CURRENT_TAB)
        parent_element = driver.find_element(By.XPATH, f".//span[text()='{name_section}']/parent::div")
        assert parent_element == activated_class