import unittest

from custom_text_test_runner import case_name
from core.test_case_base import TestCaseBase
from page_objects.bing_home_page import *

class DemoScript(TestCaseBase):
    def test_bing(self):
        #get to a URL
        self.driver.get_url("https://cn.bing.com/")
        #Input text
        SearchTextInput().input('Selenium')

        #click on a element
        SearchSubmit().click()

        # wait a element display
        SearchResultsCount().wait_element_displayed(60)

        #get a list of element
        results_list = SearchResultsList().get_elements_list()
        for result in results_list:
            print(result.text)
            #method text is native method for class selenium.webdriver.remote.webelement

        #Get property of a element
        href = WebpageTabLink().get_property('href')
        print(href)

        #Check property of a element
        #WebpageTabLink().check_property(self, 'href', "www.bing.com")

        #get text of a element
        text = WebpageTabLink().get_text()
        print(text)

        # check text of a element
        WebpageTabLink().check_text(self, '网页')

        #save screenshots to a file
        self.driver.save_screenshot()

    def test_bing2(self):
        PicTabLink().click()
        FilterLink().wait_element_displayed()
