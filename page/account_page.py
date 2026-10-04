from dataclasses import dataclass
from enum import StrEnum

import allure
from playwright.sync_api import Page, expect

from selector import account_page_selector as aps


class AccountTypeEnum(StrEnum):
    CHECKING = "CHECKING"
    SAVINGS = "SAVINGS"
    CREDIT = "CREDIT"


@dataclass
class AccountNew:
    account_name: str
    account_type: AccountTypeEnum
    starting_balance: int


@dataclass
class AccountEdit:
    account_name: str = None
    account_type: AccountTypeEnum = None
    starting_balance: int = None


def accounts_menu(page: Page):
    page.locator(aps.ACCOUNTS_MENU).click()

    with allure.step("Account Menu"):
        accounts_menu_ss = page.screenshot(full_page=True)
        allure.attach(
            accounts_menu_ss,
            "Account Menu",
            allure.attachment_type.PNG,
        )


def add_account(page: Page, acc: AccountNew):
    page.locator(aps.ADD_ACCOUNT_BTN).click()

    with allure.step("Before fill add account"):
        before_add_account_ss = page.screenshot(full_page=True)
        allure.attach(
            before_add_account_ss,
            "Before fill add account",
            allure.attachment_type.PNG,
        )

    page.locator(aps.ACCOUNT_NAME_INPUT_TXT).fill(acc.account_name)
    page.locator(aps.ACCOUNT_TYPE_SELECT_OPTION).click()
    match acc.account_type:
        case AccountTypeEnum.CHECKING:
            page.keyboard.press("Enter")
        case AccountTypeEnum.SAVINGS:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case AccountTypeEnum.CREDIT:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case _:
            pass

    page.locator(aps.STARTING_BALANCE_INPUT_TXT).fill(str(acc.starting_balance))
    page.locator(aps.TERM_AND_CONDITION_CHECKBOX).click()

    with allure.step("After fill add account"):
        after_add_account_ss = page.screenshot(full_page=True)
        allure.attach(
            after_add_account_ss,
            "After fill add account",
            allure.attachment_type.PNG,
        )

    page.locator(aps.ADD_ACCOUNT_FORM_BTN).click()

    expect(page.locator(aps.ACCOUNT_NAME_ROW).nth(-1)).to_have_text(acc.account_name)
    expect(page.locator(aps.ACCOUNT_TYPE_ROW).nth(-1)).to_have_text(
        acc.account_type.capitalize()
    )
    expected_balance = f"${float(acc.starting_balance):,.2f}"
    expect(page.locator(aps.ACCOUNT_BALANCE_ROW).nth(-1)).to_have_text(expected_balance)


def view_account(page: Page, acc: AccountNew | AccountEdit):
    page.locator(aps.VIEW_BTN).nth(-1).click()

    if acc.account_name is not None:
        expect(page.locator(aps.ACCOUNT_NAME_TXT)).to_have_text(acc.account_name)
    if acc.account_type is not None:
        expect(page.locator(aps.ACCOUNT_TYPE_TXT)).to_have_text(
            acc.account_type.capitalize()
        )
    if acc.starting_balance is not None:
        expected_balance = f"${float(acc.starting_balance):,.2f}"
        expect(page.locator(aps.ACCOUNT_BALANCE_TXT)).to_have_text(expected_balance)

    with allure.step("Account detail"):
        account_detail_ss = page.screenshot(full_page=True)
        allure.attach(
            account_detail_ss,
            "Account detail",
            allure.attachment_type.PNG,
        )


def back_to_accounts_menu(page: Page):
    page.locator(aps.BACK_TO_ACCOUNT).click()

    with allure.step("All accounts"):
        all_accounts_ss = page.screenshot(full_page=True)
        allure.attach(
            all_accounts_ss,
            "All accounts",
            allure.attachment_type.PNG,
        )


def edit_account(page: Page, acc: AccountEdit):
    page.locator(aps.EDIT_BTN).nth(-1).click()

    with allure.step("Before edit account"):
        after_edit_account_ss = page.screenshot(full_page=True)
        allure.attach(
            after_edit_account_ss,
            "Before edit account",
            allure.attachment_type.PNG,
        )

    if acc.account_name is not None:
        page.locator(aps.ACCOUNT_NAME_INPUT_TXT).fill(acc.account_name)

    if acc.account_type is not None:
        page.locator(aps.ACCOUNT_TYPE_SELECT_OPTION).click()
        match acc.account_type:
            case AccountTypeEnum.CHECKING:
                page.keyboard.press("Enter")
            case AccountTypeEnum.SAVINGS:
                page.keyboard.press("ArrowDown")
                page.keyboard.press("Enter")
            case AccountTypeEnum.CREDIT:
                page.keyboard.press("ArrowDown")
                page.keyboard.press("ArrowDown")
                page.keyboard.press("Enter")
            case _:
                pass

    if acc.starting_balance is not None:
        page.locator(aps.STARTING_BALANCE_INPUT_TXT).fill(str(acc.starting_balance))

    with allure.step("After edit account"):
        after_edit_account_ss = page.screenshot(full_page=True)
        allure.attach(
            after_edit_account_ss,
            "After edit account",
            allure.attachment_type.PNG,
        )

    page.locator(aps.SAVE_CHANGES_BTN).click()


def delete_account(page: Page, acc: AccountNew | AccountEdit):
    page.locator(aps.DELETE_BTN).nth(-1).click()

    with allure.step("Delete account"):
        delete_account_ss = page.screenshot(full_page=True)
        allure.attach(
            delete_account_ss,
            "Delete account",
            allure.attachment_type.PNG,
        )

    page.locator(aps.CONFIRM_DELETE_BTN).click()

    with allure.step("Confirm delete account"):
        delete_account_confirm_ss = page.screenshot(full_page=True)
        allure.attach(
            delete_account_confirm_ss,
            "Confirm delete account",
            allure.attachment_type.PNG,
        )

    expect(page.get_by_text(acc.account_name)).not_to_be_visible()
