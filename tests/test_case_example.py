import pytest
from pages.login_page import LoginPage
from pages.client_search_page import ClientSearchPage


@pytest.mark.demoTestCase
class TestCaseDemo:

    def test_login_page_elements_present(self, driver):
        login = LoginPage(driver)
        login.env_file_login()

        client_dash = ClientSearchPage(driver)
        client_dash.open_add_menu()


