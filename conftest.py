import pytest
from selene.support.shared import browser


@pytest.fixture()
def open_browser():
    browser.open('https://www.google.com/')
    browser.driver.maximize_window()
    yield
    browser.quit()