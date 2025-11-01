from pages.base_page import BasePage
from locators.main_locators import MainLocators


class MainPage(BasePage):
    def open_main(self):
        self.open("") 
        return self

    # кнопки "Заказать" на главной
    def click_order_top(self):
        self.click(MainLocators.ORDER_TOP_BTN)

    def click_order_bottom(self):
        self.scroll_into_view(MainLocators.ORDER_BOTTOM_BTN)
        self.click(MainLocators.ORDER_BOTTOM_BTN)

    def start_order(self, entry: str):
        """Старт оформления заказа; логика выбора кнопки скрыта внутри PageObject."""
        self.open_main()
        if entry == "from_top_button":
            self.click_order_top()
        else:
            self.click_order_bottom()

    # FAQ
    def expand_question(self, index: int):
        self.scroll_into_view(MainLocators.FAQ_QUESTION(index))
        self.click(MainLocators.FAQ_QUESTION(index))

    def get_answer_text(self, index: int) -> str:
        return self.wait_visible(MainLocators.FAQ_ANSWER(index)).text

    # Логотипы
    def click_logo_samokat(self):
        self.click(MainLocators.LOGO_SAMOKAT)

    def click_logo_yandex_new_tab(self) -> str:
        """Клик по логотипу Яндекса и переключение на вкладку Дзен. Возвращает URL новой вкладки."""
        self.click(MainLocators.LOGO_YANDEX)
        return self.switch_to_new_tab()

    def is_main_opened(self) -> bool:
        try:
            self.wait_visible(MainLocators.MAIN_MARKER)
            return True
        except Exception:
            return False