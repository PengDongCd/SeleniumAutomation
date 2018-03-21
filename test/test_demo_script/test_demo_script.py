import unittest
from core.webdriver_base import TestWebDriver
from main import browser_name


class DemoScript(unittest.TestCase):
    def setUp(self):
        self.driver = TestWebDriver(browser_name).start_webdriver()

    def test_baidu(self):
        self.driver.get("http://www.baidu.com")

    def tearDown(self):
        self.driver.quit()