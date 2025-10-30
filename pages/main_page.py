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

    # FAQ
    def expand_question(self, index: int):
        self.scroll_into_view(MainLocators.FAQ_QUESTION(index))
        self.click(MainLocators.FAQ_QUESTION(index))

    def get_answer_text(self, index: int) -> str:
        return self.wait_visible(MainLocators.FAQ_ANSWER(index)).text

    # Логотипы
    def click_logo_samokat(self):
        self.click(MainLocators.LOGO_SAMOKAT)

    def click_logo_yandex_new_tab(self):
        """Клик по логотипу Яндекса и переключение на вкладку Дзен."""
        main_handle = self.driver.current_window_handle

        # Клик по логотипу
        self.click(MainLocators.LOGO_YANDEX)

        # Ждём появления второй вкладки
        self.wait.until(lambda d: len(d.window_handles) > 1)

        # Переключаемся на новую вкладку
        for handle in self.driver.window_handles:
            if handle != main_handle:
                self.driver.switch_to.window(handle)
                break

        # Ждём, пока URL станет реальным 
        self.wait.until(
            lambda d: d.current_url and d.current_url.startswith("http") and "about:blank" not in d.current_url
        )
        return self.driver.current_url

    def is_main_opened(self) -> bool:
        try:
            self.wait_visible(MainLocators.MAIN_MARKER)
            return True
        except Exception:
            return False