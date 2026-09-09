import glob
import os

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


def get_firefox_driver():
    options = webdriver.FirefoxOptions()
    try:
        return webdriver.Firefox(options=options)
    except Exception:
        pass

    if os.path.exists("geckodriver.exe"):
        service = Service(executable_path=os.path.abspath("geckodriver.exe"))
        return webdriver.Firefox(service=service, options=options)

    wdm_cache = os.path.expanduser(r"~\.wdm\drivers\geckodriver")
    matches = glob.glob(os.path.join(wdm_cache, "**", "geckodriver.exe"), recursive=True)
    if matches:
        service = Service(executable_path=matches[0])
        return webdriver.Firefox(service=service, options=options)

    raise RuntimeError("Не удалось инициализировать Firefox WebDriver")


@pytest.fixture
def driver():
    driver = get_firefox_driver()
    driver.maximize_window()
    yield driver
    driver.quit()