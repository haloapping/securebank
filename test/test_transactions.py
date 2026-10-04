from playwright.sync_api import Page

from page import auth_page, transactions_page
from page.auth_page import LoginCredential


def test_transactions_menu(page: Page):
    lc = LoginCredential("standard_user", "bank_sauce")
    auth_page.valid_login(page, lc)

    transactions_page.transaction_menu(page)

    auth_page.logout(page)
