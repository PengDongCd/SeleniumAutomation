import unittest

from selenium import webdriver


class DemoScript(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_baidu(self):
        self.driver.get("http://www.baidu.com")

    def tearDown(self):
        self.driver.quit()