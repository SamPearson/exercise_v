from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests import config


class ElementStillPresentException(Exception):
    def __init__(self, message):
        self.message = message


class BasePage:
    def __init__(self, driver):
        # Child pages will probably overwrite this method
        # but if they don't need to, they still need a driver.
        self.driver = driver

    def _visit(self, url):
        if url.startswith("http"):
            self.driver.get(url)
        else:
            self.driver.get(config.baseurl + url)

    def _find(self, locator):
        assert self._is_displayed(locator, 2), f"Attempted to find element with the locator {locator}, but could not"
        return self.driver.find_element(locator["by"], locator["value"])

    def _find_children(self, parent, locator):
        assert self._is_displayed(locator, 2), f"Attempted to find child elements with the locator {locator}, but could not"
        children = parent.find_elements(locator["by"], locator["value"])
        if children:
            return children
        else:
            raise NoSuchElementException(f"No child elements were found with the locator {locator}")

    def _find_child(self, parent, locator):
        assert self._is_displayed(locator, 2), f"Attempted to find child element with the locator {locator}, but could not"
        return self._find_children(parent, locator)[0]

    def _find_all(self, locator):
        assert self._is_displayed(locator, 2), f"Attempted to find elements with the locator {locator}, but could not"
        elements = self.driver.find_elements(locator["by"], locator["value"])
        if elements:
            return elements
        else:
            raise NoSuchElementException(f"No elements were found with the locator {locator}")

    def _click(self, locator):
        self._find(locator).click()

    def _type(self, locator, input_text):
        self._find(locator).send_keys(input_text)

    def _is_displayed(self, locator, timeout=0):
        """Tests whether an element is present, visible, and interactive"""
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(
                    expected_conditions.visibility_of_element_located(
                        (locator['by'], locator['value'])))
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self._find(locator).is_displayed()
            except NoSuchElementException:
                return False

    def _is_present(self, locator, timeout=0):
        """Tests whether an element is present, whether visible/interactive or not"""
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(
                    expected_conditions.presence_of_element_located(
                        (locator['by'], locator['value'])))
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self._find(locator).is_present()
            except NoSuchElementException:
                return False

    def _wait_until_element_gone(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                expected_conditions.invisibility_of_element_located(
                    (locator['by'], locator['value'])))
        except TimeoutException:
            raise ElementStillPresentException(f'Waited for element to disappear but timed out after {timeout} seconds.'
                                               f' - Using locator {locator}')

