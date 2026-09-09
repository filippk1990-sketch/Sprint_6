import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Urls, OrderData


@allure.epic("Оформление заказа")
@allure.feature("Позитивный сценарий")
class TestOrderScooter:

    @pytest.mark.parametrize("entry_point, user_data", [
        ("header", OrderData.USER_1),
        ("finish", OrderData.USER_2)
    ])
    @allure.title("Заказ через точку входа: {entry_point}")
    def test_order_flow_success(self, driver, entry_point, user_data):
        main_page = MainPage(driver)
        main_page.open_url(Urls.BASE_URL)
        main_page.accept_cookies()

        if entry_point == "header":
            main_page.click_header_order_button()
        else:
            main_page.click_finish_order_button()

        order_page = OrderPage(driver)
        order_page.fill_first_step_form(
            name=user_data["name"],
            surname=user_data["surname"],
            address=user_data["address"],
            metro=user_data["metro"],
            phone=user_data["phone"]
        )

        order_page.fill_second_step_form(
            date=user_data["date"],
            rental_period=user_data["rental_period"],
            color=user_data["color"],
            comment=user_data["comment"]
        )

        order_page.confirm_order()
        assert order_page.is_order_successful()