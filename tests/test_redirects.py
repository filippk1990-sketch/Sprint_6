import allure
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from data import Urls


@allure.epic("Навигация")
@allure.feature("Редиректы с логотипов")
class TestLogoRedirects:

    @allure.title("Клик на логотип Самоката возвращает на главную")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.ORDER_URL)
        main_page.accept_cookies()

        main_page.click_scooter_logo()
        assert main_page.get_current_url() == Urls.BASE_URL

    @allure.title("Клик на логотип Яндекса переводит на Дзен")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.BASE_URL)
        main_page.accept_cookies()

        main_page.click_yandex_logo()
        main_page.switch_to_new_tab()

        WebDriverWait(driver, 10).until(
            lambda d: Urls.DZEN_URL_PART in d.current_url
        )
        assert Urls.DZEN_URL_PART in driver.current_url