import time

from selenium.common.exceptions import TimeoutException, \
    StaleElementReferenceException, UnexpectedAlertPresentException, JavascriptException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import config.base_config as config
from globals import GlobalVars as glob


class BasePage(object):

    def __init__(self):
        self.browser = glob.driver
        self.timeout = config.default_wait

    def visit(self, url):
        self.browser.get(url)
        print("Visiting url: {}".format(url))
        return self

    def find_element(self, locator, visibility=True, timeout=config.default_wait):
        try:
            if visibility:
                return WebDriverWait(self.browser, timeout=timeout).until(ec.visibility_of_element_located(locator),
                                                                          'ELEMENT IS NOT FOUND OR VISIBLE! => {}'.format(
                                                                              locator))
            else:
                return WebDriverWait(self.browser, timeout=timeout).until(ec.presence_of_element_located(locator),
                                                                          'ELEMENT IS NOT FOUND! => {}'.format(locator))
        except TimeoutException as e:
            raise TimeoutException(e.__cause__)
        except StaleElementReferenceException as e:
            raise StaleElementReferenceException(e.__cause__)

    def click_element(self, locator, timeout=config.default_wait):
        try:
            WebDriverWait(self.browser, timeout=timeout).until(ec.element_to_be_clickable(locator),
                                                                   'UNABLE TO LOCATE ELEMENT! => {}'.format(
                                                                       locator)).click()
        except TimeoutException as e:
            raise TimeoutException(e.__cause__)
        except StaleElementReferenceException as e:
            raise StaleElementReferenceException(e.__cause__)
        return self

    def fill_input(self, locator, value, timeout=config.default_wait):
        element = self.find_element(locator, timeout=timeout)
        try:
            element.send_keys(value)
        except StaleElementReferenceException as e:
            print(f"Failed to fill {value} input on {locator} with {e}")
            raise StaleElementReferenceException(e.__cause__)
        return self

    def verify_element_displayed(self, locator, timeout=config.default_wait):
        try:
            WebDriverWait(self.browser, timeout=timeout).until(
                ec.visibility_of_element_located(locator),
                f'ELEMENT EXPECTED TO BE VISIBLE IS NOT DISPLAYED! => {locator}',
            )
        except TimeoutException as e:
            raise TimeoutException(e.__cause__)
        return self

    def switch_to_window(self, index):
        self.browser.switch_to.window(self.browser.window_handles[index - 1])
        return self

    def switch_to_active_tab(self):
        driver_len = len(self.browser.window_handles)  # fetching the Number of Opened tabs
        print("Length of Driver = ", driver_len)
        if driver_len > 1:  # Will execute if more than 1 tabs found.
            self.browser.switch_to.window(self.browser.window_handles[driver_len - 1])
        else:
            print("Found only Single tab.")
