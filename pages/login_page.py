from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    _login_form = {"by": By.XPATH, "value": "//div[@data-test-login-form='true']"}
    _username_field = {"by": By.XPATH, "value": "//div[@data-test-username='true']/input"}
    _password_field = {"by": By.XPATH, "value": "//div[@data-test-password='true']/input"}
    _login_button = {"by": By.XPATH, "value": "//button[@data-test-login='true']"}
    _login_progress_indicator = {"by": By.XPATH,
                                 "value": "//button[@data-test-login='true']/span[contains(@class, 'login-loader')]"}

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
        assert self._is_displayed(self._login_form, 5), "Could not find login form"
        self._type(self._username_field, username)
        self._type(self._password_field, password)
        self._click(self._login_button)
        # Logging in can take an extremely long time.
        # We wait up to 2 seconds for a login progress indicator to appear,
        # then up to 30 more seconds for it to disappear
        if self._is_displayed(self._login_progress_indicator, 2):
            self._wait_until_element_gone(self._login_progress_indicator, 30)

    def login_error_message(self):
        self._is_displayed(self._login_error,2)
        return self._find(self._login_error).text
