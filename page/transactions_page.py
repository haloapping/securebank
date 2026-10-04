import allure
from playwright.sync_api import Page

from selector import transactions_page_selector as tps


def transaction_menu(page: Page):
    page.locator(tps.TRANSACTIONS_MENU).click()
    with allure.step("Transactions menu"):
        transactions_menu = page.screenshot(full_page=True)
        allure.attach(
            transactions_menu,
            "Transactions menu",
            allure.attachment_type.PNG,
        )
