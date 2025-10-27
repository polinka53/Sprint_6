from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logo_samokat_leads_to_home(driver, base_url):
    page = MainPage(driver, base_url)
    page.open_main(base_url)
    page.click_logo_samokat()
    assert "qa-scooter.praktikum-services.ru" in driver.current_url

def test_logo_yandex_opens_new_tab(driver, base_url):
    page = MainPage(driver, base_url)
    page.open_main(base_url)
    page.click_logo_yandex()
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[-1])
    WebDriverWait(driver, 10).until(lambda d: "yandex" in d.current_url or "dzen" in d.current_url)
    assert "yandex" in driver.current_url or "dzen" in driver.current_url, f"Не похоже на Яндекс: {driver.current_url}"