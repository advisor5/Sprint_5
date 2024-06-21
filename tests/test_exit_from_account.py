from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators

# Проверка выхода по кнопке «Выйти» в личном кабинете

class TestMesto:
    def test_exit_from_account(self, login: WebDriver):
        driver = login

        # Поиск и клик по кнопке «Выйти» в личном кабинете
        driver.find_element(*Locators.PERSONAL_EXIT).click()
        input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE)).text
        assert input == 'Вход'
        