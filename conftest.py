import glob
import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    try:
        service = Service(GeckoDriverManager().install())
    except Exception:
        # Fallback на случай исчерпания лимитов GitHub API (Rate limit exceeded)
        cache_pattern = os.path.expanduser(r"~\.wdm\drivers\geckodriver\**\geckodriver.exe")
        cached_drivers = glob.glob(cache_pattern, recursive=True)
        if cached_drivers:
            service = Service(cached_drivers[0])
        else:
            service = Service()

    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()