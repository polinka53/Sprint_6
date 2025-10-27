from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class BasePage:
    def __init__(self, driver, base_url=None):
        self.driver = driver
        self.base_url = base_url

    def open(self, url):
        self.driver.get(url)

    def wait_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def scroll_into_view(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    def click_safe(self, locator, timeout=10, retries=2):
        last_err = None
        for _ in range(retries + 1):
            try:
                el = self.wait_visible(locator, timeout)
                self.scroll_into_view(el)
                el = self.wait_clickable(locator, timeout)
                el.click()
                return
            except StaleElementReferenceException as e:
                last_err = e
        if last_err:
            raise last_err