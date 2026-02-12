import pytest
import allure
from pages.home_page import HomePage
from data import FAQ_ITEMS

@allure.feature("FAQ")
class TestFaq:
    @allure.title("Проверка раскрытия вопроса FAQ №{index}")
    @pytest.mark.parametrize("index, expected", FAQ_ITEMS)
    def test_faq_items(self, driver, index, expected):
        home = HomePage(driver)
        home.open_home()
        home.accept_cookies()
        home.click_faq_question(index)
        assert expected in home.get_faq_answer(index)