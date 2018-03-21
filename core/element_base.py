import logging

import selenium
from selenium import webdriver

class ElementBase:
    def __init__(self,find_method, find_value, driver):
        self.find_method = find_method
        self.find_value = find_value
        self.driver = webdriver.Chrome

    def find_element(self):
        try:
            if self.find_method == 'xpath':
                return self.driver.find_element_by_xpath(self.find_value)
            elif self.find_method == 'class_name':
                return self.driver.find_element_by_class_name(self.find_value)
            elif self.find_method == 'id':
                return self.driver.find_element_by_id(self.find_value)
            elif self.find_method == 'name':
                return self.driver.find_element_by_name(self.find_value)
            elif self.find_method == 'tag_name':
                return self.driver.find_element_by_tag_name(self.find_value)
            elif self.find_method == 'link_text':
                return self.driver.find_element_by_link_text(self.find_value)
            elif self.find_method == 'partial_link_text':
                return self.driver.find_element_by_partial_link_text(self.find_value)
            elif self.find_method == 'css_selector':
                return self.driver.find_element_by_css_selector(self.find_value)
        except selenium.common.exceptions.NoSuchElementException:
            return None
    def find_elements(self):
        try:
            if self.find_method == 'xpath':
                return self.driver.find_elements_by_xpath(self.find_value)
            elif self.find_method == 'class_name':
                return self.driver.find_elements_by_class_name(self.find_value)
            elif self.find_method == 'id':
                return self.driver.find_elements_by_id(self.find_value)
            elif self.find_method == 'name':
                return self.driver.find_elements_by_name(self.find_value)
            elif self.find_method == 'tag_name':
                return self.driver.find_elements_by_tag_name(self.find_value)
            elif self.find_method == 'link_text':
                return self.driver.find_elements_by_link_text(self.find_value)
            elif self.find_method == 'partial_link_text':
                return self.driver.find_elements_by_partial_link_text(self.find_value)
            elif self.find_method == 'css_selector':
                return self.driver.find_elements_by_css_selector(self.find_value)
        except selenium.common.exceptions.NoSuchElementException:
            return None

    def click(self):
        element = self.find_element()
        if element:
            element.click()
        else:
            logging.error("Error! This element don't exist")



