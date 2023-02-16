

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ClientDashboardPage(BasePage):

    def __init__(self, driver, name):
        self.driver = driver

        self._client_action_menu = {"by": By.XPATH, "value": "//a[@data-test-clientactions ='true']"}
        # self._add_button
        # self._add_button_menu
        # self._add_goal_button
        # self._add_income_button
        # self._add_insurance_button

        assert self._is_displayed(self._client_action_menu, 5)
        assert self._find(self._client_action_menu).text == name['last'] + ", " + name['first']


