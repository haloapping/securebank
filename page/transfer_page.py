from dataclasses import dataclass
from enum import StrEnum

import allure
from playwright.sync_api import Page

from selector import transfer_page_selector as tps


def transfer_menu(page: Page):
    page.locator(tps.TRANSFER_MENU).click()

    with allure.step("Transfer menu"):
        transfer_menu_ss = page.screenshot(full_page=True)
        allure.attach(
            transfer_menu_ss,
            "Transfer menu",
            allure.attachment_type.PNG,
        )


class AccountEnum(StrEnum):
    FIRST_ACCOUNT = "FIRST_ACCOUNT"
    SECOND_ACCOUNT = "SECOND_ACCOUNT"
    THIRD_ACCOUNT = "THIRD_ACCOUNT"


class TransferDateEnum(StrEnum):
    TODAY = "TODAY"
    SCHEDULE = "SCHEDULE"


@dataclass
class CreateTransfer:
    from_account: AccountEnum
    to_account: AccountEnum
    amount: int
    transfer_date: TransferDateEnum
    memo: str = None
    select_date_transfer: str = None


def create_transfer(page: Page, trf: CreateTransfer):
    page.locator(tps.FROM_ACCOUNT_SELECT_OPTION).click()
    match trf.from_account:
        case AccountEnum.FIRST_ACCOUNT:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case AccountEnum.SECOND_ACCOUNT:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case AccountEnum.SECOND_ACCOUNT:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")

    page.locator(tps.TO_ACCOUNT_SELECT_OPTION).click()
    match trf.from_account:
        case AccountEnum.FIRST_ACCOUNT:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case AccountEnum.SECOND_ACCOUNT:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case AccountEnum.SECOND_ACCOUNT:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case _:
            pass

    page.locator(tps.AMOUNT_INPUT_TXT).fill(str(trf.amount))

    if trf.memo is not None:
        page.locator(tps.MEMO_INPUT_TXT).fill(trf.memo)

    match trf.transfer_date:
        case TransferDateEnum.TODAY:
            page.locator(tps.TRANSFER_DATE_TODAY_RADIO_BTN).click()
        case TransferDateEnum.SCHEDULE:
            page.locator(tps.TRANSFER_DATE_SCHEDULE_RADIO_BTN).click()
            page.click(tps.SCHEDULE_DATE_INPUT_TXT)

            page.keyboard.press("ArrowLeft")
            page.keyboard.press("ArrowLeft")

            date_part = trf.select_date_transfer.split("/")
            day = date_part[0]
            page.keyboard.type(day)
            month = date_part[1]
            page.keyboard.type(month)
            year = date_part[2]
            page.keyboard.type(year)

    with allure.step("Create transfer"):
        create_transfer_ss = page.screenshot(full_page=True)
        allure.attach(
            create_transfer_ss,
            "Create transfer",
            allure.attachment_type.PNG,
        )

    page.locator(tps.REVIEW_TRANSFER_BTN).click()

    with allure.step("Confirm transfer"):
        confirm_transfer_ss = page.screenshot(full_page=True)
        allure.attach(
            confirm_transfer_ss,
            "Confirm transfer",
            allure.attachment_type.PNG,
        )

    page.locator(tps.CONFIRM_TRANSFER_BTN).click()

    with allure.step("Transfer successful"):
        transfer_successful_ss = page.screenshot(full_page=True)
        allure.attach(
            transfer_successful_ss,
            "Transfer successful",
            allure.attachment_type.PNG,
        )


def back_to_transfer_menu(page: Page):
    page.locator(tps.BACK_TO_TRANSFER_MENU_BTN).click()

    with allure.step("Back to transfer menu"):
        back_to_transfer_menu_ss = page.screenshot(full_page=True)
        allure.attach(
            back_to_transfer_menu_ss,
            "Back to transfer menu",
            allure.attachment_type.PNG,
        )


def make_another_transfer(page: Page):
    page.locator(tps.MAKE_ANOTHER_TRANSFER_BTN).click()

    with allure.step("Make another transfer"):
        make_another_transfer_ss = page.screenshot(full_page=True)
        allure.attach(
            make_another_transfer_ss,
            "Make another transfer",
            allure.attachment_type.PNG,
        )
