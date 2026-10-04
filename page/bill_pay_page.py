from dataclasses import dataclass
from enum import StrEnum

import allure
from playwright.sync_api import Page

from selector import bill_pay_page_selector as bpps


def bill_pay_menu(page: Page):
    page.locator(bpps.BILL_PAY_MENU).click()

    with allure.step("Bill Pay menu"):
        dashboard_menu_ss = page.screenshot(full_page=True)
        allure.attach(
            dashboard_menu_ss,
            "Bill Pay menu",
            allure.attachment_type.PNG,
        )


class FromAccountEnum(StrEnum):
    EVERYDAY_CHECKING = "EVERYDAY_CHECKING"
    HIGH_YIELD_SAVINGS = "HIGH_YIELD_SAVINGS"


@dataclass
class Bill:
    from_account: FromAccountEnum
    biller: str
    amount: int
    payment_date: str
    memo: str = None


def bill_pay(page: Page, b: Bill):
    page.locator(bpps.FROM_ACCOUNT_DROPDOWN_LIST).click()
    match b.from_account:
        case FromAccountEnum.EVERYDAY_CHECKING:
            page.keyboard.press("Enter")
        case FromAccountEnum.HIGH_YIELD_SAVINGS:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")

    page.locator(bpps.BILLER_INPUT_TXT).fill(b.biller)
    page.locator(bpps.BILLER_SEARCH_RESULT).nth(0).click()
    page.locator(bpps.AMOUNT_INPUT_TXT).fill(str(b.amount))

    page.locator(bpps.PAYMENT_DATE_INPUT_TXT).click()
    page.keyboard.press("ArrowLeft")
    page.keyboard.press("ArrowLeft")
    date_parts = b.payment_date.split("/")
    page.keyboard.type(date_parts[0])
    page.keyboard.type(date_parts[1])
    page.keyboard.type(date_parts[2])

    if b.memo is not None:
        page.locator(bpps.MEMO_INPUT_TXT).fill(b.memo)

    with allure.step("Bill payment form"):
        bill_payment_form_ss = page.screenshot(full_page=True)
        allure.attach(
            bill_payment_form_ss,
            "Bill payment form",
            allure.attachment_type.PNG,
        )

    page.locator(bpps.REVIEW_PAYMENT_BTN).click()

    with allure.step("Confirm bill payment"):
        confirm_bill_payment_ss = page.screenshot(full_page=True)
        allure.attach(
            confirm_bill_payment_ss,
            "Confirm bill payment",
            allure.attachment_type.PNG,
        )

    page.locator(bpps.CONFIRM_PAYMENT_BTN).click()

    with allure.step("Bill payment success"):
        bill_payment_success_ss = page.screenshot(full_page=True)
        allure.attach(
            bill_payment_success_ss,
            "Bill payment success",
            allure.attachment_type.PNG,
        )


def back_to_bill_pay(page: Page):
    page.locator(bpps.BACK_TO_BILL_PAY_BTN).click()

    with allure.step("Back to Bill Pay menu"):
        dashboard_menu_ss = page.screenshot(full_page=True)
        allure.attach(
            dashboard_menu_ss,
            "Back to Bill Pay menu",
            allure.attachment_type.PNG,
        )


def pay_another_bill(page: Page):
    page.locator(bpps.PAY_ANOTHER_BILL_BTN).click()

    with allure.step("Pay Another Bill"):
        dashboard_menu_ss = page.screenshot(full_page=True)
        allure.attach(
            dashboard_menu_ss,
            "Pay Another Bill",
            allure.attachment_type.PNG,
        )
