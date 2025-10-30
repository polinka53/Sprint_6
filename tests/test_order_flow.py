import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data.order_data import CASES

@allure.title("Оформление заказа самоката (позитивный сценарий)")
@pytest.mark.parametrize("case", CASES, ids=lambda c: c["entry"])
def test_order_scooter_positive(driver, base_url, case):
    entry = case["entry"]
    if entry == "from_top_button":
        page = OrderPage(driver, base_url)
        page.open_order()
    else:
        main = MainPage(driver, base_url)
        main.open_main()
        main.click_order_bottom()
        page = OrderPage(driver, base_url)

    d = case["data"]
    page.fill_first_form(d["name"], d["surname"], d["address"], d["metro"], d["phone"])
    page.fill_second_form(d["date"], d["color"], "сутки", d["comment"])
    page.submit_and_confirm()