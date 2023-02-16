
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ClientSearchPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

        self._release_notes_modal = {"by": By.ID, "value": "data-entry-modal"}
        self._release_notes_close_button = {"by": By.XPATH, "value": "//button[contains(@class, 'test-modal-close')]"}

        self._client_list_table = {"by": By.XPATH, "value": "//table[@data-test-client-list ='true']"}
        self._client_list_row = {"by": By.XPATH, "value": "//tr[@data-test-client-row='true']"}
        self._client_name_cell = {"by": By.CLASS_NAME, "value": "name-text"}

        self._add_button = {"by": By.XPATH, "value": "//button[@data-test-add-button='true']"}

        self.verify_client_table_displayed()

    def verify_client_table_displayed(self):
        assert self._is_present(self._client_list_table, 5), "Could not find client table, " \
                                                               "may not be at client search page"
        assert self._is_present(self._client_list_row, 5), "Could not find any rows in client table, " \
                                                               "may not be at client search page"

    def clear_release_notes_modal(self):
        if self._is_displayed(self._release_notes_modal):
            modal = self._find(self._release_notes_modal)
            self._find_child(modal, self._release_notes_close_button).click()
            self._wait_until_element_gone(self._release_notes_modal)
            assert self._is_displayed(self._client_list_row)

    def client_list(self):

        clients = []

        for row in self._find_all(self._client_list_row):
            name = self._find_child(row, self._client_name_cell).text
            clients.append({
                'name': name
            })
        return clients

    def client_exists(self, name):
        self.verify_client_table_displayed()
        clients = self.client_list()
        for c in clients:
            if c['name'] == name['last'] + ", " + name['first']:
                return True
        return False

    def open_new_client_dialog(self):
        self._click(self._add_button)


class NewClientModal(BasePage):

    def __init__(self, driver):
        self.driver = driver

        self._new_client_dialog = {"by": By.XPATH, "value": "//div[@data-test-edit-container-modal ='true']"}
        self._first_name_input = {"by": By.XPATH, "value": "//div[@data-test-firstname ='true']//input"}
        self._last_name_input = {"by": By.XPATH, "value": "//div[@data-test-lastname ='true']//input"}
        self._birth_year_input = {"by": By.XPATH, "value": "//div[@data-test-birthdayyear ='true']//input"}

        self._done_button = {"by": By.XPATH, "value": "//button[@data-test-model-save='true']"}

        # Required but prefilled fields:
        # plan start date (day/month/year)
        # Retirement age
        # Not required:
        # province

    def create_new_client(self, name):
        self._type(self._first_name_input, name['first'])
        self._type(self._last_name_input, name['last'])
        self._type(self._birth_year_input, "1990")

        self._click(self._done_button)
        self._wait_until_element_gone(self._new_client_dialog)
