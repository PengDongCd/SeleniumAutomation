import logging
import unittest
from time import sleep
from core.webdriver_base import TestWebDriver
import selenium
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

class ElementBase:
    def __init__(self,find_method, find_value, test_driver: TestWebDriver):
        self.find_method = find_method
        self.find_value = find_value
        self.test_driver = test_driver
        self.element = None

    def get_element(self):
        try:
            self.element = self.test_driver.find_element(self)
        except selenium.common.exceptions.NoSuchElementException:
            logging.error("Error! This element doesn't exist!")
        if self.element:
            logging.info("Found element by {method} with {value}".format(method=self.find_method, value=self.find_value))
            return self.element
        else:
            logging.error("Error! This element is None!")


    def get_elements_list(self):
        self.elements = self.test_driver.find_elements(self)
        if self.elements:
            logging.info("Found elements list by {method} with {value}".format(method=self.find_method, value=self.find_value))
            return self.elements
        else:
            logging.error("Error! These elements doesn't exist!")

    def is_visible(self):
        if self.get_element():
            if self.element.is_displayed():
                logging.info("This element ID={id} is visible on page!".format(id=self.element.id))
                return True

            else:
                logging.info("This element ID={id} is NOT visible on page!".format(id=self.element.id))
                return False

    def click(self):
        if self.is_visible():
            self.test_driver.driver.execute_script('arguments[0].scrollIntoView(true);', self.element)
            try:
                self.element.click()
                logging.info("Click on element ID={id} succeed".format(id=self.element.id))
            except Exception:
                logging.error("Click on element ID={id} failed".format(id=self.element.id))
        else:
            logging.error("Error! This element ID={id} is NOT visible on page so you can click on it!".format(id=self.element.id))

    def input(self, input_str):
        self.get_element()
        self.element.send_keys(input_str)
        logging.info("Input text {text} in element {id} succeed".format(text=input_str, id=self.element.id))

    def wait_element_displayed(self, timeout=10):
        #self.get_element()
        for i in range(timeout+1):
            if self.is_visible():
                logging.info("The element ID={id} is displayed on page now after waiting for {w_time} seconds!".format(id=self.element.id, w_time=i))
                break
            elif i == timeout:
                logging.error("The element ID={id} is NOT displayed on page \
                               now after waiting for {timeout} seconds!".format(id=self.element.id, timeout=timeout))
            else:
                sleep(1)

    def wait_until(self, timeout, func):
        wait = WebDriverWait(self.test_driver.driver, timeout)
        wait.until(func)

    def get_property(self, p_name):
        self.get_element()
        if self.element.get_attribute(p_name): #Attributes are defined by HTML. Properties are defined by DOM.
            logging.info("Assert! Got the property or attribute {name}!".format(name=p_name))
            return self.element.get_attribute(p_name)
        else:
            logging.error("Failed to get the property or attribute {name}!".format(name=p_name))

    def check_property(self, tc, p_name, expected_property):
        actual_property = self.get_property(p_name)
        tc.assertEqual(actual_property, expected_property, "Comparing The property {p_name}'s value of element ID={id}".format(p_name=p_name,
                                                                        id=self.element.id))
    def get_text(self):
        self.get_element()
        try:
            logging.info("Assert! Got text of element ID={id} is {text}!".format(id=self.element.id, text=self.element.text))
            return self.element.text
        except Exception:
            logging.error("Failed to get TEXT of element ID={id}".format(id=self.element.id))

    def check_text(self, tc, text):
        tc.assertEqual(self.get_text(), text, "Comparing The text of element ID={id}".format(id=self.element.id))

    def is_enabled(self):
        if self.is_visible():
            if self.element.is_enabled():
                logging.info("Assert! The element ID={id} is enabled! ".format(id=self.element.id))
            else:
                logging.error("Error! The element ID={id} is NOT enabled! ".format(id=self.element.id))
