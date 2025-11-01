from selenium.webdriver.common.by import By

class OrderLocators:
    # Первая форма
    NAME     = (By.XPATH, "//input[contains(@placeholder,'Имя')]")
    SURNAME  = (By.XPATH, "//input[contains(@placeholder,'Фамил')]")
    ADDRESS  = (By.XPATH, "//input[contains(@placeholder,'Адрес')]")
    METRO    = (By.XPATH, "//input[contains(@placeholder,'Станц')]")
    PHONE    = (By.XPATH, "//input[contains(@placeholder,'Телефон')]")
    NEXT_BTN = (By.XPATH, "//button[normalize-space()='Далее']")

    # Выпадающий список метро
    METRO_OPTIONS_CONTAINER = (By.XPATH, "//div[contains(@class,'select-search__select')]")
    @staticmethod
    def METRO_OPTION_BY_TEXT(name: str):
        return (By.XPATH, f"//div[contains(@class,'select-search__row')]//div[normalize-space()='{name}']/parent::button")
    ANY_METRO_OPTION = (By.XPATH, "//div[contains(@class,'select-search__row')]//button")

    # Вторая форма
    DATE          = (By.XPATH, "//input[contains(@placeholder,'Когда привезти')]")
    PERIOD_OPEN   = (By.XPATH, "//div[contains(@class,'Dropdown-control')]")
    @staticmethod
    def PERIOD_OPTION(text: str):
        return (By.XPATH, f"//div[contains(@class,'Dropdown-menu')]//div[normalize-space()='{text}']")
    COLOR_BLACK   = (By.ID, "black")
    COLOR_GREY    = (By.ID, "grey")
    COMMENT       = (By.XPATH, "//input[contains(@placeholder,'Комментарий') or contains(@placeholder,'курьер')]")
    ORDER_SUBMIT  = (By.XPATH, "//div[contains(@class,'Order_Buttons')]/button[normalize-space()='Заказать']")

    MODAL      = (By.XPATH, "//div[contains(@class,'Order_Modal') or contains(@class,'Modal')][.//button]")
    YES_BTN    = (By.XPATH, "//div[contains(@class,'Modal') or contains(@class,'Order_Modal')]//button[normalize-space()='Да']")