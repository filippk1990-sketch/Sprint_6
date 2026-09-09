import pytest
import allure
from pages.main_page import MainPage
from data import Urls, FaqAnswers


@allure.epic("Главная страница")
@allure.feature("Вопросы о важном")
class TestFaqAccordion:

    @pytest.mark.parametrize("index, expected_answer", list(enumerate(FaqAnswers.ANSWERS)))
    @allure.title("Проверка вопроса FAQ #{index}")
    def test_faq_accordion_item(self, driver, index, expected_answer):
        main_page = MainPage(driver)
        main_page.open_url(Urls.BASE_URL)
        main_page.accept_cookies()

        main_page.click_faq_question(index)
        actual_answer = main_page.get_faq_answer_text(index)

        assert actual_answer == expected_answer