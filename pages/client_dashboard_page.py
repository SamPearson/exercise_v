

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ClientDashboardPage(BasePage):

    def __init__(self, driver, name):
        self.driver = driver

        self._client_action_menu = {"by": By.XPATH, "value": "//a[@data-test-clientactions ='true']"}
        self._add_button = {"by": By.XPATH, "value": "//a[@data-test-add-button ='true']"}
        self._add_button_menu = {"by": By.CLASS_NAME, "value": "add-button-menu"}

        self._add_goal_button = {"by": By.XPATH, "value": "//button[@data-test-model-type ='goals']"}
        self._add_income_button = {"by": By.XPATH, "value": "//button[@data-test-model-type ='income']"}
        self._add_insurance_button = {"by": By.XPATH, "value": "//button[@data-test-model-type ='protection']"}

        assert self._is_displayed(self._client_action_menu, 5)
        assert self._find(self._client_action_menu).text == name['last'] + ", " + name['first']

    def _open_add_menu(self):
        if not self._is_displayed(self._add_button_menu):
            self._click(self._add_button)

