from playwright.sync_api import Page

from page import auth_page
from page.auth_page import LoginCredential


def test_valid_login(page: Page):
    lc = LoginCredential("standard_user", "bank_sauce")
    auth_page.valid_login(page, lc)

    auth_page.logout(page)


def test_invalid_login(page: Page):
    lc = LoginCredential("standard_userr", "bank_sauce")
    auth_page.invalid_login(page, lc)
