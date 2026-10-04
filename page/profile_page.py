from enum import StrEnum

import allure
from playwright.sync_api import Page, expect

from selector import profile_page_selector as pps


def profile_menu(page: Page):
    page.locator(pps.PROFILE_MENU).click()

    with allure.step("Profile menu"):
        profile_menu_ss = page.screenshot(full_page=True)
        allure.attach(
            profile_menu_ss,
            "Profile menu",
            allure.attachment_type.PNG,
        )


class UsernameEnum(StrEnum):
    STANDARD_USER = "STANDARD_USER"
    FROZEN_USER = "FROZEN_USER"
    OVERDRAFT_USER = "OVERDRAFT_USER"
    SLOW_USER = "SLOW_USER"
    ERROR_USER = "ERROR_USER"
    ADMIN_USER = "ADMIN_USER"


def detail_profile(page: Page, username: UsernameEnum):
    match username:
        case UsernameEnum.STANDARD_USER:
            expect(page.locator(pps.USERNAME_TXT)).to_have_text("standard_user")
            expect(page.locator(pps.FIRST_NAME_TXT)).to_have_text("Alex")
            expect(page.locator(pps.LAST_NAME_TXT)).to_have_text("Morgan")
            expect(page.locator(pps.EMAIL_TXT)).to_have_text("alex.morgan@example.com")
            expect(page.locator(pps.PHONE_TXT)).to_have_text("(415) 555-0101")
            expect(page.locator(pps.ADDRESS_TXT)).to_have_text(
                "123 Market Street, San Francisco, CA 94105"
            )
        case UsernameEnum.FROZEN_USER:
            expect(page.locator(pps.USERNAME_TXT)).to_have_text("frozen_user")
            expect(page.locator(pps.FIRST_NAME_TXT)).to_have_text("Jordan")
            expect(page.locator(pps.LAST_NAME_TXT)).to_have_text("Lee")
            expect(page.locator(pps.EMAIL_TXT)).to_have_text("jordan.lee@example.com")
            expect(page.locator(pps.PHONE_TXT)).to_have_text("(415) 555-0303")
            expect(page.locator(pps.ADDRESS_TXT)).to_have_text(
                "789 Howard Street, San Francisco, CA 94103"
            )
        case UsernameEnum.OVERDRAFT_USER:
            expect(page.locator(pps.USERNAME_TXT)).to_have_text("overdraft_user")
            expect(page.locator(pps.FIRST_NAME_TXT)).to_have_text("Casey")
            expect(page.locator(pps.LAST_NAME_TXT)).to_have_text("Rivera")
            expect(page.locator(pps.EMAIL_TXT)).to_have_text("casey.rivera@example.com")
            expect(page.locator(pps.PHONE_TXT)).to_have_text("(415) 555-0404")
            expect(page.locator(pps.ADDRESS_TXT)).to_have_text(
                "321 Folsom Street, San Francisco, CA 94107"
            )
        case UsernameEnum.SLOW_USER:
            expect(page.locator(pps.USERNAME_TXT)).to_have_text("slow_user")
            expect(page.locator(pps.FIRST_NAME_TXT)).to_have_text("Morgan")
            expect(page.locator(pps.LAST_NAME_TXT)).to_have_text("Chen")
            expect(page.locator(pps.EMAIL_TXT)).to_have_text("morgan.chen@example.com")
            expect(page.locator(pps.PHONE_TXT)).to_have_text("(415) 555-0505")
            expect(page.locator(pps.ADDRESS_TXT)).to_have_text(
                "555 California Street, San Francisco, CA 94104"
            )
        case UsernameEnum.ERROR_USER:
            expect(page.locator(pps.USERNAME_TXT)).to_have_text("error_user")
            expect(page.locator(pps.FIRST_NAME_TXT)).to_have_text("Riley")
            expect(page.locator(pps.LAST_NAME_TXT)).to_have_text("Nguyen")
            expect(page.locator(pps.EMAIL_TXT)).to_have_text("riley.nguyen@example.com")
            expect(page.locator(pps.PHONE_TXT)).to_have_text("(415) 555-0606")
            expect(page.locator(pps.ADDRESS_TXT)).to_have_text(
                "88 Bryant Street, San Francisco, CA 94107"
            )
        case UsernameEnum.ADMIN_USER:
            expect(page.locator(pps.USERNAME_TXT)).to_have_text("admin_user")
            expect(page.locator(pps.FIRST_NAME_TXT)).to_have_text("Admin")
            expect(page.locator(pps.LAST_NAME_TXT)).to_have_text("User")
            expect(page.locator(pps.EMAIL_TXT)).to_have_text(
                "admin@securebank.example.com"
            )
            expect(page.locator(pps.PHONE_TXT)).to_have_text("(415) 555-0001")
            expect(page.locator(pps.ADDRESS_TXT)).to_have_text(
                "1 SecureBank Plaza, San Francisco, CA 94111"
            )
        case _:
            pass
