from playwright.sync_api import Page
from page import auth_page, notification_page
from page.auth_page import LoginCredential


def test_notification(page: Page):
    lc = LoginCredential("admin_user", "admin_sauce")
    auth_page.valid_login(page, lc)

    notification_page.notification_menu(page)
    notification_page.check_notif(page)

    auth_page.logout(page)
