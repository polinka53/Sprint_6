import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

BASE_URL = "https://qa-scooter.praktikum-services.ru/"
FIREFOX_BIN = r"C:\Users\ASUS\AppData\Local\Mozilla Firefox\firefox.exe"
GECKO_PATH = r"C:\Users\ASUS\Documents\Sprint_6\drivers\geckodriver.exe"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def headless():
    return False

@pytest.fixture(scope="function")
def driver(headless, base_url):
    options = FirefoxOptions()
    if headless:
        options.add_argument("-headless")

    options.binary_location = FIREFOX_BIN
    service = FirefoxService(GECKO_PATH)
    driver = webdriver.Firefox(service=service, options=options)
    driver.set_window_size(1366, 900)
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    with allure.step("Закрываем браузер"):
        driver.quit()