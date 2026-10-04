from playwright.sync_api import Page

from page import auth_page, transfer_page
from page.auth_page import LoginCredential
from page.transfer_page import AccountEnum, CreateTransfer, TransferDateEnum


def test_create_transfer(page: Page):
    lc = LoginCredential("standard_user", "bank_sauce")
    auth_page.valid_login(page, lc)

    transfer_page.transfer_menu(page)
    trf = CreateTransfer(
        from_account=AccountEnum.FIRST_ACCOUNT,
        to_account=AccountEnum.FIRST_ACCOUNT,
        amount=5,
        memo="TRX",
        transfer_date=TransferDateEnum.SCHEDULE,
        select_date_transfer="10/10/2026",
    )
    transfer_page.create_transfer(page, trf)
    transfer_page.back_to_transfer_menu(page)

    auth_page.logout(page)
