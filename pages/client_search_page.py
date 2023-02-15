

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ClientSearchPage(BasePage):
    _client_list_table = {"by": By.XPATH, "value": "//table[@data-test-client-list ='true']"}
    _release_notes_modal = {"by": By.ID, "value": "data-entry-modal"}
    _release_notes_close_button = {"by": By.XPATH, "value": "//button[contains(@class, 'test-modal-close')]"}

    _add_button = {"by": By.XPATH, "value": "//button[@data-test-add-button='true']"}

    def __init__(self, driver):
        self.driver = driver

        assert self._is_present(self._client_list_table, 5), "Could not find client table, " \
                                                               "may not be at client search page"

        if self._is_displayed(self._release_notes_modal):
            modal = self._find(self._release_notes_modal)
            self._find_child(modal, self._release_notes_close_button).click()
            self._wait_until_element_gone(self._release_notes_modal)

    def verify_elements_present(self):
        assert self._is_present(self._client_list_table), "Could not find client table, "

    def open_add_menu(self):
        self._click(self._add_button)


class NewClientModal(BasePage):
    def __init__(self, driver):
        self.driver = driver
