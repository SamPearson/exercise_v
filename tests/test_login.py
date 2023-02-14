import pytest
from pages.login_page import LoginPage


class TestLogin:
    @pytest.fixture
    def login_page(self, driver):
        return LoginPage(driver)

    def test_login_page_elements_present(self, login_page):
        login_page.verify_elements_present()

    def test_incorrect_login(self, login_page):
        login_page.log_in("incorrect_username", "incorrect_password")
        assert login_page.login_error_message() == "Incorrect credentials"
