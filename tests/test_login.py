import pytest
from pages import login_page


class TestLogin:
    @pytest.fixture
    def login_page(self, driver):
        return login_page.LoginPage(driver)

    def test_login_page_elements_present(self, login_page):
        login_page.verify_elements_present()

