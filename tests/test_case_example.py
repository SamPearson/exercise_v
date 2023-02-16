import pytest
from pages.login_page import LoginPage
from pages.client_search_page import ClientSearchPage, NewClientModal
from pages.client_dashboard_page import ClientDashboardPage
import names


@pytest.mark.demoTestCase
class TestCaseDemo:

    def test_login(self, driver):
        login = LoginPage(driver)
        login.env_file_login()

        client_dash = ClientSearchPage(driver)

    def test_add_client(self, driver):
        LoginPage(driver).env_file_login()

        client_search_page = ClientSearchPage(driver)
        client_search_page.clear_release_notes_modal()

        name = {
            'first': names.get_first_name(),
            'last': names.get_last_name()
        }

        client_search_page.open_new_client_dialog()
        new_client_modal = NewClientModal(driver)
        new_client_modal.create_new_client(name)

        client_dash = ClientDashboardPage(driver, name)

    def test_add_pre_retirement_goal(self, driver):
        LoginPage(driver).env_file_login()

        client_search_page = ClientSearchPage(driver)
        client_search_page.clear_release_notes_modal()

        name = {
            'first': names.get_first_name(),
            'last': names.get_last_name()
        }

        client_search_page.open_new_client_dialog()
        new_client_modal = NewClientModal(driver)
        new_client_modal.create_new_client(name)

        client_dash = ClientDashboardPage(driver, name)
        # Stopped due to questions about modals in page object model.

