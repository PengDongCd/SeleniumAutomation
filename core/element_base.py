import logging
from core.webdriver_base import TestWebDriver
import selenium
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

class ElementBase:
    def __init__(self,find_method, find_value, driver: TestWebDriver):
        self.find_method = find_method
        self.find_value = find_value
        self.driver = driver
        self.element = None

    def get_element(self):
        self.element = self.driver.find_element(self)
        if self.element:
            logging.info("Found element by {method} with {value}".format(method=self.find_method, value=self.find_value))
            return self.element
        else:
            logging.error("Error! This element doesn't exist!")

    def is_visible(self):
        self.get_element()
        if self.element.is_displayed():
            logging.info("This element ID={id} is visible on page!".format(id=self.element.id))
            return True

        else:
            logging.info("This element ID={id} is NOT visible on page!".format(id=self.element.id))
            return False

    def click(self):
        if self.is_visible():
            self.element.click()
        else:
            logging.error("Error! This element ID={id} is NOT visible on page so you can click on it!".format(id=self.element.id))

    def input(self, input_str):
        self.get_element()
        self.element.send_keys(input_str)

    def wait_element_displayed(self, timeout=30):
        self.get_element()
        wait = WebDriverWait(self.driver.driver, timeout)
        wait.until(lambda dr: self.is_visible(), 'Wait for Element ID={id} and it is displayed now!'.format(id=self.element.id))