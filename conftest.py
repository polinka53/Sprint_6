import pytest
from selenium import webdriver
from data.urls import BASE_URL


@pytest.fixture
def driver():
    drv = webdriver.Firefox()
    drv.get(BASE_URL)
    yield drv
    drv.quit()


@pytest.fixture
def base_url():
    return BASE_URL