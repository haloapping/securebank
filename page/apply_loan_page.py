from dataclasses import dataclass
from enum import StrEnum

import allure
from playwright.sync_api import Page

from selector import apply_loan_page_selector as alps


def apply_loan_menu(page: Page):
    page.locator(alps.APPLY_LOAN_MENU).click()

    with allure.step("Apply loan menu"):
        apply_loan_menu_ss = page.screenshot(full_page=True)
        allure.attach(
            apply_loan_menu_ss,
            "Apply loan menu",
            allure.attachment_type.PNG,
        )


class LoanTypeEnum(StrEnum):
    PERSONAL = "PERSONAL"
    AUTO = "AUTO"
    HOME = "HOME"
    STUDENT = "STUDENT"


class TermLengthEnum(StrEnum):
    MONTHS_12 = "12_MONTHS"
    MONTHS_24 = "24_MONTHS"
    MONTHS_36 = "26_MONTHS"
    MONTHS_48 = "48_MONTHS"
    MONTHS_60 = "60_MONTHS"


class DisbursementAccountEnum(StrEnum):
    EVERYDAY_CHECKING = "EVERYDAY_CHECKING"
    HIGH_YIELD_SAVINGS = "HIGH_YIELD_SAVINGS"


@dataclass
class Loan:
    loan_type: LoanTypeEnum
    loan_amount: int
    term_length: TermLengthEnum
    interest_rate: float
    disbursement_account: DisbursementAccountEnum
    purpose: str


def apply_loan(page: Page, loan: Loan):
    page.locator(alps.APPLY_FOR_LOAN_BTN).click()

    page.locator(alps.LOAN_TYPE_DROPDOWN_LIST).click()
    match loan.loan_type:
        case LoanTypeEnum.PERSONAL:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case LoanTypeEnum.AUTO:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case LoanTypeEnum.HOME:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case LoanTypeEnum.STUDENT:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case _:
            pass

    page.locator(alps.LOAN_AMOUNT_INPUT_TXT).fill(str(loan.loan_amount))

    page.locator(alps.TERM_LENGTH_DROPDOWN_LIST).click()
    match loan.term_length:
        case TermLengthEnum.MONTHS_12:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case TermLengthEnum.MONTHS_24:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case TermLengthEnum.MONTHS_36:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case TermLengthEnum.MONTHS_48:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case TermLengthEnum.MONTHS_60:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case _:
            pass

    page.locator(alps.INTEREST_RATE_INPUT_TXT).fill(str(loan.interest_rate))

    page.locator(alps.DISBURSEMENT_ACCOUNT_DROPDOWN_LIST).click()
    match loan.disbursement_account:
        case DisbursementAccountEnum.EVERYDAY_CHECKING:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case DisbursementAccountEnum.HIGH_YIELD_SAVINGS:
            page.keyboard.press("ArrowDown")
            page.keyboard.press("ArrowDown")
            page.keyboard.press("Enter")
        case _:
            pass

    page.locator(alps.PURPOSE_INPUT_TXT).fill(loan.purpose)

    with allure.step("Apply loan form"):
        apply_loan_form_ss = page.screenshot(full_page=True)
        allure.attach(
            apply_loan_form_ss,
            "Apply loan form",
            allure.attachment_type.PNG,
        )

    page.locator(alps.REVIEW_APPLICATION_BTN).click()

    with allure.step("Confirm apply loan"):
        confirm_apply_loan_ss = page.screenshot(full_page=True)
        allure.attach(
            confirm_apply_loan_ss,
            "Confirm apply loan",
            allure.attachment_type.PNG,
        )

    page.locator(alps.SUBMIT_APPLICATION_BTN).click()

    with allure.step("Apply loan success"):
        apply_loan_success_ss = page.screenshot(full_page=True)
        allure.attach(
            apply_loan_success_ss,
            "Apply loan success",
            allure.attachment_type.PNG,
        )
