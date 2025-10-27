from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 15)

    def open(self, path=""):
        self.driver.get(self.base_url + (path or ""))

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        el.click()
        return el

    def js_click(self, locator):
        el = self.find(locator)
        self.driver.execute_script("arguments[0].click();", el)
        return el


class OrderPage(BasePage):
    # форма 1
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[contains(@class,'select-search__input')]")
    METRO_WIDGET = (By.XPATH, "//div[contains(@class,'select-search__select')]")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BTN = (By.XPATH, "//button[.='Далее']")

    # куки
    COOKIE_BTN = (By.XPATH, "//button[contains(.,'да все') or contains(.,'понятно') or contains(.,'Да, всё понятно')]")

    # форма 2
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-root']")
    RENT_OPTION_TWO_DAYS = (By.XPATH, "//div[contains(@class,'Dropdown-menu')]//div[normalize-space()='двое суток']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BTN = (By.XPATH, "//button[.='Заказать']")

    # подтверждение
    YES_BTN = (By.XPATH, "//button[.='Да']")

    def accept_cookies_if_shown(self):
        try:
            self.click(self.COOKIE_BTN)
        except Exception:
            pass

    def start_from(self, entry):
        if entry == "from_top_button":
            self.click((By.XPATH, "//div[contains(@class,'Header')]/button[.='Заказать']"))
        else:
            self.click((By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button[.='Заказать']"))

    def _select_metro(self, metro_text):
        self.click(self.METRO_FIELD)
        fld = self.find(self.METRO_FIELD)
        fld.clear()
        fld.send_keys(metro_text[:3])
        self.wait.until(EC.visibility_of_element_located(self.METRO_WIDGET))
        fld.send_keys(Keys.ARROW_DOWN)
        fld.send_keys(Keys.ENTER)
        self.wait.until(EC.text_to_be_present_in_element_value(self.METRO_FIELD, ""))  

    def fill_first_form(self, name, surname, address, metro, phone):
        self.accept_cookies_if_shown()
        self.click(self.NAME).send_keys(name)
        self.click(self.SURNAME).send_keys(surname)
        self.click(self.ADDRESS).send_keys(address)
        self._select_metro(metro)
        self.click(self.PHONE).send_keys(phone)
        self.click(self.NEXT_BTN)

    def _set_date(self, date_str):
        self.click(self.DATE_FIELD)
        fld = self.find(self.DATE_FIELD)
        fld.clear()
        fld.send_keys(date_str)
        fld.send_keys(Keys.ENTER)
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class,'react-datepicker__tab-loop')]")))

    def _set_rent_period_two_days(self):
        self.click(self.RENT_DROPDOWN)
        try:
            self.click(self.RENT_OPTION_TWO_DAYS)
        except Exception:
            self.js_click(self.RENT_OPTION_TWO_DAYS)

    def fill_second_form(self, date_str, comment, color="black"):
        self._set_date(date_str)
        self._set_rent_period_two_days()
        if color == "black":
            self.js_click(self.COLOR_BLACK)
        else:
            self.js_click(self.COLOR_GREY)
        self.click(self.COMMENT).send_keys(comment)

    def submit_and_confirm(self):
        order_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'Order_Buttons')]/button[text()='Заказать']")
            )
        )
        order_btn.click()

        yes_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Да']"))
        )
        yes_btn.click()