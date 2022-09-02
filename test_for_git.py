import pytest
from selene.support.shared import browser


@pytest.fixture()
def open_browser():
    browser.open('https://google.com')
    browser.config.window_width = 1500
    browser.config.window_height = 1500


def test_for_git(open_browser):
    pass
