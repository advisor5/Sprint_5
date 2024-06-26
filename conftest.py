import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators
from constants import Url
import random


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Url.HOST)
    yield browser
    browser.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.MAIN_PERSONAL_AC).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.IN_PAGE))

    driver.find_element(*Locators.IN_FIELD_EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.IN_FIELD_PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.IN_BUTTON).click()
    return driver

@pytest.fixture
def gen_email():
    email = f"sergei_kravchuk10{random.randint(100, 999)}@ya.ru"
    return email