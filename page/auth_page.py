import os
from dataclasses import dataclass

import allure
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

from selector import auth_page_selector as aps


@dataclass
class LoginCredential:
    username: str
    password: str


def valid_login(page: Page, lc: LoginCredential):
    load_dotenv()

    page.goto(os.getenv("BASE_URL"))

    with allure.step("Before fill login form"):
        before_fill_login_ss = page.screenshot(full_page=True)
        allure.attach(
            before_fill_login_ss,
            "Before fill login form",
            allure.attachment_type.PNG,
        )

    page.locator(aps.USERNAME_INPUT_TXT).fill(lc.username)
    page.locator(aps.PASSWORD_INPUT_TXT).fill(lc.password)

    with allure.step("After fill login form"):
        after_fill_login_ss = page.screenshot(full_page=True)
        allure.attach(
            after_fill_login_ss,
            "After fill login form",
            allure.attachment_type.PNG,
        )

    page.locator(aps.SIGN_IN_BTN).click()

    expect(page).to_have_url("https://qaplayground.com/bank/dashboard")

    with allure.step("Dashboard page"):
        dashboard_ss = page.screenshot(full_page=True)
        allure.attach(
            dashboard_ss,
            "Dashboard page",
            allure.attachment_type.PNG,
        )


def invalid_login(page: Page, lc: LoginCredential):
    load_dotenv()

    page.goto(os.getenv("BASE_URL"))

    with allure.step("Before fill login form"):
        before_fill_login_ss = page.screenshot(full_page=True)
        allure.attach(
            before_fill_login_ss,
            "Before fill login form",
            allure.attachment_type.PNG,
        )

    page.locator(aps.USERNAME_INPUT_TXT).fill(lc.username)
    page.locator(aps.PASSWORD_INPUT_TXT).fill(lc.password)

    with allure.step("After fill login form"):
        after_fill_login_ss = page.screenshot(full_page=True)
        allure.attach(
            after_fill_login_ss,
            "After fill login form",
            allure.attachment_type.PNG,
        )

    page.locator(aps.SIGN_IN_BTN).click()

    expect(page).to_have_url("https://qaplayground.com/bank/login")
    expect(page.locator(aps.LOGIN_ERR_MSG)).to_have_text(
        "The username or password you entered is incorrect."
    )

    with allure.step("Login Error"):
        login_err_ss = page.screenshot(full_page=True)
        allure.attach(
            login_err_ss,
            "Login Error",
            allure.attachment_type.PNG,
        )


def logout(page: Page):
    page.locator(aps.LOGOUT_BTN).click()

    with allure.step("Logout"):
        logout_ss = page.screenshot(full_page=True)
        allure.attach(
            logout_ss,
            "Logout",
            allure.attachment_type.PNG,
        )
