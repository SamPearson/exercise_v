from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    _login_form = {"by": By.XPATH, "value": "//div[@data-test-login-form='true']"}
    _username_field = {"by": By.XPATH, "value": "//div[@data-test-username='true']"}
    _password_field = {"by": By.XPATH, "value": "//div[@data-test-password='true']"}
    _login_button = {"by": By.XPATH, "value": "//button[@data-test-login='true']"}

    _login_error = {"by": By.XPATH, "value": "//div[@data-test-noaccesserror='true']"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("/#/login")

    def verify_elements_present(self):
        assert self._is_displayed(self._login_form, 5), "Could not find login form"
        assert self._is_displayed(self._username_field), "Could not find username field"
        assert self._is_displayed(self._password_field), "Could not find password field"
        assert self._is_displayed(self._login_button), "Could not find login button"

    def log_in(self, username, password):
        self._type(self._username_field, username)
        self._type(self._password_field, password)
        self._click(self._login_button)
