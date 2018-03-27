import unittest
from main import browser_name
from .webdriver_base import TestWebDriver
from .element_base import ElementBase

class TestCaseBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = TestWebDriver(browser_name)
        cls.driver.start_webdriver()
        ElementBase.test_driver = cls.driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit_webdriver()

    def setUp(self):
        self.driver = self.get_test_driver()

    def tearDown(self):
        self.driver.save_screenshot('tear_down')

    @classmethod
    def get_test_driver(cls):
        return cls.driver
