import pytest
from selenium import webdriver
from pages.order_page import OrderPage

cases = [
    {
        "entry": "from_top_button",
        "data": {
            "name": "Полина",
            "surname": "Павлицкая",
            "address": "Проспект Мира 6",
            "metro": "Охотный Ряд",
            "phone": "+77055531278",
            "date": "27.10.2025",
            "comment": "Самокат должен быть чистым",
        },
    },
    {
        "entry": "from_bottom_button",
        "data": {
            "name": "Анна",
            "surname": "Иванова",
            "address": "Тверская 12",
            "metro": "Пушкинская",
            "phone": "+78888888888",
            "date": "27.10.2025",
            "comment": "Оставить у двери",
        },
    },
]

@pytest.fixture
def base_url():
    return "https://qa-scooter.praktikum-services.ru/"

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.set_window_position(0, 0)
    driver.set_window_size(1280, 900)
    yield driver
    driver.quit()
    
import allure

@allure.feature("Order")
@allure.story("Positive flow")
@allure.title("Оформление заказа: {entry}")
@pytest.mark.parametrize("entry,data", [(c["entry"], c["data"]) for c in cases], ids=["data0","data1"])
def test_order_scooter_positive(driver, base_url, entry, data):
    page = OrderPage(driver, base_url)
    page.open()
    page.start_from(entry)

    page.fill_first_form(
        data["name"], data["surname"], data["address"], data["metro"], data["phone"]
    )

    page.fill_second_form(
        data["date"], data["comment"], color="black"
    )

    page.submit_and_confirm()