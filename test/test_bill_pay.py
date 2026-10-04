from playwright.sync_api import Page

from page import auth_page, bill_pay_page
from page.auth_page import LoginCredential
from page.bill_pay_page import Bill, FromAccountEnum


def test_bill_pay_success(page: Page):
    lc = LoginCredential("standard_user", "bank_sauce")
    auth_page.valid_login(page, lc)

    bill_pay_page.bill_pay_menu(page)
    b = Bill(
        FromAccountEnum.HIGH_YIELD_SAVINGS,
        "Metro Water Utility",
        1000,
        "11/11/2026",
    )
    bill_pay_page.bill_pay(page, b)

    auth_page.logout(page)
