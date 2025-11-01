from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
)


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url.rstrip("/") + "/"
        self.wait = WebDriverWait(driver, 12)

    # навигация
    def open(self, path: str = ""):
        url = self.base_url + path.lstrip("/")
        self.driver.get(url)
        self.close_cookies_if_present()

    # ожидания/поиск/клики/ввод
    def wait_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find(self, locator):
        return self.driver.find_element(*locator)

    def js_click(self, el):
        self.driver.execute_script("arguments[0].click();", el)

    def scroll_into_view(self, locator):
        el = self.wait_present(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        return el

    def click(self, locator):
        try:
            self.wait_clickable(locator).click()
        except (TimeoutException, ElementClickInterceptedException, StaleElementReferenceException):
            el = self.scroll_into_view(locator)
            try:
                el.click()
            except Exception:
                self.js_click(el)

    def type(self, locator, text: str, clear=True):
        el = self.wait_visible(locator)
        if clear:
            el.clear()
        el.send_keys(text)

    # утилиты
    def close_cookies_if_present(self):
        try:
            btns = self.driver.find_elements(
                By.XPATH,
                "//button[contains(@class,'Cookie') or contains(.,'привыкли') or contains(.,'cookies')]",
            )
            if btns:
                self.driver.execute_script("arguments[0].click();", btns[0])
        except Exception:
            pass

    def switch_to_new_tab(self) -> str:
        """Ждём открытия новой вкладки, переключаемся на неё и возвращаем реальный URL."""
        main_handle = self.driver.current_window_handle
        self.wait.until(lambda d: len(d.window_handles) > 1)

        for handle in self.driver.window_handles:
            if handle != main_handle:
                self.driver.switch_to.window(handle)
                break

        self.wait.until(
            lambda d: d.current_url and d.current_url.startswith("http") and "about:blank" not in d.current_url
        )
        return self.driver.current_url