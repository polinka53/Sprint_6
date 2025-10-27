from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
    # локаторы
    FAQ_QUESTION = lambda self, i: (By.ID, f"accordion__heading-{i}")
    FAQ_ANSWER = lambda self, i: (By.ID, f"accordion__panel-{i}")
    LOGO_SAMOKAT = (By.CSS_SELECTOR, "img[alt='Scooter']")
    LOGO_YANDEX = (By.CSS_SELECTOR, "img[alt='Yandex']")

    def open_main(self, base_url):
        self.open(base_url)

    def expand_question(self, index):
        self.click_safe(self.FAQ_QUESTION(index))

    def get_answer_text(self, index):
        el = self.wait_visible(self.FAQ_ANSWER(index))
        return el.text

    def click_logo_samokat(self):
        self.click_safe(self.LOGO_SAMOKAT)

    def click_logo_yandex(self):
        self.click_safe(self.LOGO_YANDEX)