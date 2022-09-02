import pytest
from selene.support.shared import browser


@pytest.fixture()
def open_browser():
    browser.open('https://google.com')


def test_for_git(open_browser):
    pass
