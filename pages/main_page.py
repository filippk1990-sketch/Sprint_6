import allure
from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            self.click_element(MainPageLocators.COOKIE_BUTTON)
        except Exception:
            pass

    @allure.step("Кликнуть по верхней кнопке «Заказать»")
    def click_header_order_button(self):
        self.click_element(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step("Кликнуть по нижней кнопке «Заказать»")
    def click_finish_order_button(self):
        self.scroll_to_element(MainPageLocators.FINISH_ORDER_BUTTON)
        self.click_element(MainPageLocators.FINISH_ORDER_BUTTON)

    @allure.step("Открыть вопрос FAQ с номером {index}")
    def click_faq_question(self, index):
        question_locator = MainPageLocators.get_question_locator(index)
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)

    @allure.step("Получить текст ответа FAQ с номером {index}")
    def get_faq_answer_text(self, index):
        answer_locator = MainPageLocators.get_answer_locator(index)
        return self.get_text(answer_locator)

    @allure.step("Кликнуть по логотипу «Самокат»")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Кликнуть по логотипу «Яндекс»")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)