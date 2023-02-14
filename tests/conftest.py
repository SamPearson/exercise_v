
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from . import config


def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action="store",
                     default="https://ca-test.planwithvoyant.com/advisergo",
                     help="Base URL for the application under test")


@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption("--baseurl")

    driver_ = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    def quit_browser():
        driver_.quit()

    driver_.base_url = config.baseurl
    request.addfinalizer(quit_browser)
    return driver_

