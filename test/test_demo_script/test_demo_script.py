import unittest
from core.webdriver_base import TestWebDriver
from main import browser_name
from page_objects.bing_home_page import *

class DemoScript(unittest.TestCase):
    def setUp(self):
        self.driver = TestWebDriver(browser_name)
        self.driver.start_webdriver()

    def test_baidu(self):
        #get to a URL
        self.driver.get_url("https://cn.bing.com/")

        #Input text
        SearchTextInput(self.driver).input('Selenium')

        #click on a element
        SearchSubmit(self.driver).click()

        # wait a element display
        SearchResultsCount(self.driver).wait_element_displayed(60)

        #get a list of element
        results_list = SearchResultsList(self.driver).get_elements_list()
        for result in results_list:
            print(result.text)
            #method text is native method for class selenium.webdriver.remote.webelement

        #Get property of a element
        href = WebpageTabLink(self.driver).get_property('href')
        print(href)

        #Check property of a element
        #WebpageTabLink(self.driver).check_property(self, 'href', "www.bing.com")

        #get text of a element
        text = WebpageTabLink(self.driver).get_text()
        print(text)

        # check text of a element
        WebpageTabLink(self.driver).check_text(self, '网页')

        #save scrrenshot to a file
        self.driver.save_screenshot()


    def tearDown(self):
        self.driver.quit_webdriver()