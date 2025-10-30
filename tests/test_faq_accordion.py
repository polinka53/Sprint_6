import pytest
import allure
from pages.main_page import MainPage
from data.faq_texts import FAQ_ANSWERS

@allure.title("FAQ: у каждого вопроса открывается корректный текст ответа")
@pytest.mark.parametrize("index", range(8))
def test_faq_item_expands(driver, base_url, index):
    page = MainPage(driver, base_url)
    page.open_main()
    page.expand_question(index)
    text = page.get_answer_text(index).strip()
    assert text == FAQ_ANSWERS[index]