from playwright.sync_api import Page

from page import auth_page, profile_page
from page.auth_page import LoginCredential
from page.profile_page import UsernameEnum


def test_profile_detail(page: Page):
    lc = LoginCredential("admin_user", "admin_sauce")
    auth_page.valid_login(page, lc)

    profile_page.profile_menu(page)
    profile_page.detail_profile(page, UsernameEnum.ADMIN_USER)

    auth_page.logout(page)
