from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_locators import OrderLocators

class OrderPage(BasePage):
    def open_order(self):
        self.open("order")
        return self

    def fill_first_form(self, name, surname, address, metro, phone):
        self.type(OrderLocators.NAME, name)
        self.type(OrderLocators.SURNAME, surname)
        self.type(OrderLocators.ADDRESS, address)
        self.type(OrderLocators.METRO, metro)
        self.wait_present(OrderLocators.METRO_OPTIONS_CONTAINER)
        try:
            self.click(OrderLocators.METRO_OPTION_BY_TEXT(metro))
        except Exception:
            field = self.find(OrderLocators.METRO)
            field.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

        self.type(OrderLocators.PHONE, phone)
        self.click(OrderLocators.NEXT_BTN)
        return self

    def fill_second_form(self, date, color, period, comment):
        self.type(OrderLocators.DATE, date)
        self.find(OrderLocators.DATE).send_keys(Keys.ENTER)

        self.click(OrderLocators.PERIOD_OPEN)
        self.click(OrderLocators.PERIOD_OPTION(period))

        if color.lower().startswith("black") or color.startswith("ч"):
            self.click(OrderLocators.COLOR_BLACK)
        else:
            self.click(OrderLocators.COLOR_GREY)

        self.type(OrderLocators.COMMENT, comment)
        return self

   
    def submit_and_confirm(self):
        self.scroll_into_view(OrderLocators.ORDER_SUBMIT)
        self.click(OrderLocators.ORDER_SUBMIT)
        self.wait_present(OrderLocators.MODAL)
        self.click(OrderLocators.YES_BTN)
        return self
    