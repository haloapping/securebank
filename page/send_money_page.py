from dataclasses import dataclass
from enum import StrEnum

import allure
from playwright.sync_api import Page, expect

from selector import send_money_selector as sms


def send_money_menu(page: Page):
    page.locator(sms.SEND_MONEY_MENU).click()
    with allure.step("Send money menu"):
        profile_menu_ss = page.screenshot(full_page=True)
        allure.attach(
            profile_menu_ss,
            "Send money menu",
            allure.attachment_type.PNG,
        )


def back_to_send_money_menu(page: Page):
    page.locator(sms.BACK_TO_SEND_MONEY).click()
    with allure.step("Back to send money menu"):
        profile_menu_ss = page.screenshot(full_page=True)
        allure.attach(
            profile_menu_ss,
            "Back to send money menu",
            allure.attachment_type.PNG,
        )


def send_money_again(page: Page):
    page.locator(sms.SEND_MONEY_AGAIN_BTN).click()
    with allure.step("Send money again menu"):
        profile_menu_ss = page.screenshot(full_page=True)
        allure.attach(
            profile_menu_ss,
            "Send money again menu",
            allure.attachment_type.PNG,
        )


class FromAccountEnum(StrEnum):
    EVERYDAY_CHECKING = "EVERYDAY_CHECKING"
    HIGH_YIELD_SAVINGS = "HIGH-YIELD_SAVINGS"


class ToAccountEnum(StrEnum):
    RAHUL_SHARMA = "RAHUL_SHARMA"
    PRIYA_MEHTA = "PRIYA_MEHTA"
    AMIT_VERMA = "AMIT_VERMA"


@dataclass
class SendMoney:
    from_account: FromAccountEnum
    to_account: ToAccountEnum
    amount: int
    note: str = None


def send_money(page: Page, sd: SendMoney):
    page.locator(sms.FROM_ACCOUNT_DROPDOWN_LIST).click()
    match sd.from_account:
        case FromAccountEnum.EVERYDAY_CHECKING:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case FromAccountEnum.HIGH_YIELD_SAVINGS:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case _:
            pass

    page.locator(sms.PAYEE_DROPDOWN_LIST).click()
    match sd.to_account:
        case ToAccountEnum.RAHUL_SHARMA:
            page.keyboard.press("Enter")
        case ToAccountEnum.PRIYA_MEHTA:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case ToAccountEnum.PRIYA_MEHTA:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case _:
            pass

    page.locator(sms.AMOUNT_INPUT_TXT).fill(str(sd.amount))

    if sd.note is not None:
        page.locator(sms.NOTE_INPUT_TXT).fill(sd.note)

    with allure.step("Send money form"):
        send_money_form_ss = page.screenshot(full_page=True)
        allure.attach(
            send_money_form_ss,
            "Send money form",
            allure.attachment_type.PNG,
        )

    page.locator(sms.REVIEW_AND_SEND_BTN).click()

    with allure.step("Confirm send money"):
        confirm_send_money_ss = page.screenshot(full_page=True)
        allure.attach(
            confirm_send_money_ss,
            "Confirm send money",
            allure.attachment_type.PNG,
        )

    page.locator(sms.CONFIRM_SEND_BTN).click()

    expect(page.locator(sms.FROM_ACCOUNT_CONFIRM)).to_have_text(
        sd.from_account.replace("_", " ").title()
    )

    expect(page.locator(sms.TO_ACCOUNT_CONFIRM)).to_have_text(
        sd.to_account.replace("_", " ").title()
    )
    actual_amount = (
        page.locator(sms.AMOUNT_ACCOUNT_CONFIRM)
        .inner_text()
        .replace("$", "")
        .replace(",", "")
        .replace(".00", "")
    )
    assert str(sd.amount) == actual_amount

    with allure.step("Send money success"):
        send_money_success_ss = page.screenshot(full_page=True)
        allure.attach(
            send_money_success_ss,
            "Send money success",
            allure.attachment_type.PNG,
        )
