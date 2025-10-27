import pytest
from pages.main_page import MainPage

@pytest.mark.parametrize("index", range(8))
def test_faq_item_expands(driver, base_url, index):
    page = MainPage(driver, base_url)
    page.open_main(base_url)
    page.expand_question(index)
    text = page.get_answer_text(index)
    assert text.strip() != "", f"Ответ для вопроса {index} пуст!"