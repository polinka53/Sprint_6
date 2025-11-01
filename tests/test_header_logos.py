import allure
from pages.main_page import MainPage


@allure.title("Клик по логотипу Самокат ведёт на главную страницу")
def test_logo_samokat_leads_to_home(driver, base_url):
    page = MainPage(driver, base_url)
    page.open("order")
    page.click_logo_samokat()
    assert page.is_main_opened()


@allure.title("Клик по логотипу Яндекс открывает Дзен в новом окне")
def test_logo_yandex_opens_dzen(driver, base_url):
    page = MainPage(driver, base_url)
    page.open_main()
    url = page.click_logo_yandex_new_tab()
    assert url.startswith("http")