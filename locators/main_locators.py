from selenium.webdriver.common.by import By

class MainLocators:
    # Кнопки "Заказать" на главной
    ORDER_TOP_BTN    = (By.XPATH, "//div[contains(@class,'Header_Nav') or contains(@class,'Header')]" 
                                  "//button[normalize-space()='Заказать']")
    ORDER_BOTTOM_BTN = (By.XPATH, "//div[contains(@class,'Home_FinishButton') or contains(@class,'Home_Finish')]"
                                  "//button[normalize-space()='Заказать']")

    # Лого
    LOGO_SAMOKAT = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
    LOGO_YANDEX  = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")

    # Маркёр главной страницы 
    MAIN_MARKER = (By.XPATH, "//div[contains(@class,'Home_Header') or contains(@class,'Home_SubHeader')]")

    # FAQ
    @staticmethod
    def FAQ_QUESTION(i: int):
        return (By.ID, f"accordion__heading-{i}")

    @staticmethod
    def FAQ_ANSWER(i: int):
        return (By.ID, f"accordion__panel-{i}")