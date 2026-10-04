from playwright.sync_api import Page

from page import apply_loan_page, auth_page
from page.apply_loan_page import (
    DisbursementAccountEnum,
    Loan,
    LoanTypeEnum,
    TermLengthEnum,
)
from page.auth_page import LoginCredential


def test_apply_loan_success(page: Page):
    lc = LoginCredential("standard_user", "bank_sauce")
    auth_page.valid_login(page, lc)

    apply_loan_page.apply_loan_menu(page)
    loan = Loan(
        LoanTypeEnum.AUTO,
        10000,
        TermLengthEnum.MONTHS_48,
        4.5,
        DisbursementAccountEnum.HIGH_YIELD_SAVINGS,
        "Apply Loan",
    )
    apply_loan_page.apply_loan(page, loan)

    auth_page.logout(page)
