import pytest
from selene.support.shared import browser


@pytest.fixture()
def open_browser():
    browser.open('https://google.com')
    browser.config.window_height = 1450
    browser.config.window_width = 1800

def test_for_git(open_browser):
    pass
