from pages.login_page import LoginPage

from utilities.config import (
    VALID_EMAIL,
    VALID_PASSWORD,
    INVALID_EMAIL_FORMAT,
    WRONG_PASSWORD,
)


def test_valid_login(driver):

    login = LoginPage(driver)

    login.enter_email(VALID_EMAIL)
    login.enter_password(VALID_PASSWORD)

    login.click_login()

    assert "home" in driver.current_url.lower()


def test_invalid_password(driver):

    login = LoginPage(driver)

    login.enter_email(VALID_EMAIL)
    login.enter_password(WRONG_PASSWORD)

    login.click_login()

    assert "incorrect password" in login.get_error_message().lower()


def test_empty_login(driver):

    login = LoginPage(driver)

    login.click_login()

    assert login.get_error_message() != ""


def test_invalid_email_format(driver):

    login = LoginPage(driver)

    login.enter_email(INVALID_EMAIL_FORMAT)
    login.enter_password(VALID_PASSWORD)

    login.click_login()

    assert "invalid email" in login.get_error_message().lower()