from faker import Faker
from playwright.sync_api import Page

from page import account_page, auth_page
from page.account_page import AccountNew, AccountEdit, AccountTypeEnum
from page.auth_page import LoginCredential


def test_accounts(page: Page):
    lc = LoginCredential("standard_user", "bank_sauce")
    auth_page.valid_login(page, lc)

    account_page.accounts_menu(page)

    faker = Faker(locale="id_ID")
    acc = AccountNew(
        faker.first_name() + " " + faker.last_name(), AccountTypeEnum.SAVINGS, 1234
    )
    account_page.add_account(page, acc)

    account_page.view_account(page, acc)
    account_page.back_to_accounts_menu(page)

    acc_edit = AccountEdit(starting_balance=10000)
    account_page.edit_account(page, acc_edit)
    account_page.view_account(page, acc_edit)
    account_page.back_to_accounts_menu(page)

    if acc_edit.account_name is not None:
        account_page.delete_account(page, acc_edit)
    else:
        account_page.delete_account(page, acc)

    auth_page.logout(page)
