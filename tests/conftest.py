import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from utils.constants import Constants

@pytest.fixture()
def driver():
    options = webdriver.FirefoxOptions()
    options.page_load_strategy = 'eager'
    # options.add_argument("--headless")  # Запуск в headless-режиме, если нужно
    options.add_argument("--no-sandbox")

    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)

    driver.maximize_window()
    driver.get(Constants.base_url)

    yield driver

    driver.quit()
    print("Browser is closed")