import time

import pytest
from selenium.common.exceptions import NoSuchElementException

from tests.selenium_support import close_driver, get_host_for_selenium_testing, initialize_driver

pytestmark = pytest.mark.e2e


def test_notepad_index():

    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Open the index page
        driver.get(f"{host}/notepad")

        # Wait a little while to make sure the page has loaded completely
        time.sleep(4)

        try:

            pass

        except NoSuchElementException:
            raise AssertionError("Test failed!")

    finally:

        # Close the browser
        close_driver(driver)
