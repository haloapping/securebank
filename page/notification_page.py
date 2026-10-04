import allure
from playwright.sync_api import Page, expect
from selector import notification_page_selector as nps


def notification_menu(page: Page):
    page.locator(nps.NOTIFICATION_MENU).click()

    with allure.step("Before mark read"):
        before_mark_read_ss = page.screenshot(full_page=True)
        allure.attach(
            before_mark_read_ss,
            "Before mark read",
            allure.attachment_type.PNG,
        )


def check_notif(page: Page):
    curr_side_bar_notif_number = page.locator(nps.SIDE_BAR_NOTIF_BADGE).inner_text()
    curr_top_bar_notif_number = page.locator(nps.TOP_BAR_NOTIF_BADGE).inner_text()

    assert curr_side_bar_notif_number == curr_top_bar_notif_number

    page.locator(nps.SIDE_BAR_NOTIF_BADGE).click()

    page.locator(nps.MARK_READ_BTN).nth(0).click()
    curr_side_bar_notif_number = page.locator(nps.SIDE_BAR_NOTIF_BADGE).inner_text()
    curr_top_bar_notif_number = page.locator(nps.TOP_BAR_NOTIF_BADGE).inner_text()
    assert curr_side_bar_notif_number == curr_top_bar_notif_number

    page.locator(nps.MARK_READ_BTN).nth(0).click()
    expect(page.locator(nps.SIDE_BAR_NOTIF_BADGE)).not_to_be_visible()
    expect(page.locator(nps.TOP_BAR_NOTIF_BADGE)).not_to_be_visible()

    with allure.step("After mark read"):
        after_mark_read_ss = page.screenshot(full_page=True)
        allure.attach(
            after_mark_read_ss,
            "After mark read",
            allure.attachment_type.PNG,
        )
