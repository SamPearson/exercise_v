from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests import config


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _visit(self, url):
        if url.startswith("http"):
            self.driver.get(url)
        else:
            self.driver.get(config.baseurl + url)

    def _find(self, locator):
        return self.driver.find_element(locator["by"], locator["value"])

    def _find_children(self, parent, locator):
        children = parent.find_elements(locator["by"], locator["value"])
        if children:
            return children
        else:
            raise NoSuchElementException(f"No child elements were found with the locator {locator}")

    def _find_child(self, parent, locator):
        return self._find_children(parent, locator)[0]

    def _find_all(self, locator):
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
            e = self._find(locator)
            if e:
                return e.is_displayed()
            else:
                return False

    def _wait_until_element_gone(self, locator, timeout=10):
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(
                    expected_conditions.invisibility_of_element_located(
                        (locator['by'], locator['value'])))
            except TimeoutException:
                return False
            return True
        else:
            if not self._is_displayed(locator):
                return True
            else:
                return False
