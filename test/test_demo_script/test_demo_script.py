import unittest
from core.webdriver_base import TestWebDriver
from main import browser_name
from page_objects.netease_home_page import *

class DemoScript(unittest.TestCase):
    def setUp(self):
        self.driver = TestWebDriver(browser_name)
        self.driver.start_webdriver()

    def test_baidu(self):
        self.driver.get_url("http://www.163.com")
        link = SportNewsLink(self.driver)
        link.wait_element_displayed(5)

    def tearDown(self):
        self.driver.quit_webdriver()