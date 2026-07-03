from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.config import DEFAULT_TIMEOUT


class LoginPage:

    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginButton")

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "[data-testid='login-error']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def enter_email(self, email):
        field = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        field.clear()
        field.send_keys(email)

    def enter_password(self, password):
        field = self.driver.find_element(*self.PASSWORD_INPUT)
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        element = self.wait.until(
            EC.visibility_of_element_located(
                self.ERROR_MESSAGE
            )
        )
        return element.text