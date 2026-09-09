import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Заполнить первый шаг: Для кого самокат")
    def fill_first_step_form(self, name, surname, address, metro, phone):
        self.set_text(OrderPageLocators.NAME_INPUT, name)
        self.set_text(OrderPageLocators.SURNAME_INPUT, surname)
        self.set_text(OrderPageLocators.ADDRESS_INPUT, address)

        metro_field = self.find_element(OrderPageLocators.METRO_INPUT)
        metro_field.click()
        metro_field.send_keys(metro)
        metro_field.send_keys(Keys.ARROW_DOWN)
        metro_field.send_keys(Keys.ENTER)

        self.set_text(OrderPageLocators.PHONE_INPUT, phone)
        self.scroll_to_element(OrderPageLocators.NEXT_BUTTON)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить второй шаг: Про аренду")
    def fill_second_step_form(self, date, rental_period, color, comment):
        date_element = self.find_element(OrderPageLocators.DATE_INPUT)
        date_element.send_keys(date)
        date_element.send_keys(Keys.ENTER)

        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        period_option = (By.XPATH, OrderPageLocators.RENTAL_PERIOD_OPTION_TEMPLATE.format(rental_period))
        self.click_element(period_option)

        if color == "black":
            self.click_element(OrderPageLocators.COLOR_BLACK_CHECKBOX)
        elif color == "grey":
            self.click_element(OrderPageLocators.COLOR_GREY_CHECKBOX)

        self.set_text(OrderPageLocators.COMMENT_INPUT, comment)
        self.scroll_to_element(OrderPageLocators.ORDER_SUBMIT_BUTTON)
        self.click_element(OrderPageLocators.ORDER_SUBMIT_BUTTON)

    @allure.step("Подтвердить заказ в модальном окне")
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_MODAL_YES_BUTTON)

    @allure.step("Проверить успешность создания заказа")
    def is_order_successful(self):
        element = self.find_element(OrderPageLocators.SUCCESS_ORDER_HEADER)
        return element.is_displayed()