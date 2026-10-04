import allure
from playwright.sync_api import Page
from selector import dashboard_page_selector as dps


def dashboard(page: Page):
    page.locator(dps.DASHBOARD_MENU).click()

    with allure.step("Dashboard menu"):
        dashboard_menu_ss = page.screenshot(full_page=True)
        allure.attach(
            dashboard_menu_ss,
            "Dashboard menu",
            allure.attachment_type.PNG,
        )
