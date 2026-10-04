from playwright.sync_api import Page

from page import auth_page, send_money_page
from page.auth_page import LoginCredential
from page.send_money_page import FromAccountEnum, SendMoney, ToAccountEnum


def test_send_money_success(page: Page):
    lc = LoginCredential("standard_user", "bank_sauce")
    auth_page.valid_login(page, lc)

    sd = SendMoney(
        FromAccountEnum.HIGH_YIELD_SAVINGS,
        ToAccountEnum.RAHUL_SHARMA,
        1432,
    )
    send_money_page.send_money_menu(page)
    send_money_page.send_money(page, sd)

    auth_page.logout(page)
