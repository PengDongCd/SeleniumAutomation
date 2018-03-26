import selenium
import time
from selenium import webdriver
import logging
import os

DOWNLOAD_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'outputs', 'download')
if not os.path.exists(DOWNLOAD_PATH):
    os.mkdir(DOWNLOAD_PATH)
SCREENSHOOT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'outputs', 'screenshots')
if not os.path.exists(SCREENSHOOT_PATH):
    os.mkdir(SCREENSHOOT_PATH)

class TestWebDriver:
    def __init__(self, browser_name):
        self.browser_name = browser_name
        self.driver = None

    def start_webdriver(self):
        if self.browser_name == 'Firefox':
            ff_profile = webdriver.FirefoxProfile()
            ff_profile.set_preference("browser.download.folderList",2)
            ff_profile.set_preference("browser.download.dir", DOWNLOAD_PATH)
            ff_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf,text/csv,application/zip")
            self.driver = webdriver.Firefox(firefox_profile=ff_profile)
        elif self.browser_name == 'Chrome':
            chrome_opts = webdriver.ChromeOptions()
            prefs = {"download.default_directory": DOWNLOAD_PATH, "download.prompt_for_download":False}
            chrome_opts.add_experimental_option("prefs", prefs)
            chrome_opts.add_argument('--disable-extensions')
            chrome_opts.add_argument('--disable-popup-blocking')
            chrome_opts.add_argument('--ignore-certificate-errors')
            chrome_opts.add_argument('--test-type')
            chrome_opts.add_argument('--headless')
            chrome_opts.add_argument('--disable-gpu')
            #chrome_opts.add_argument('--remote-debugging-port=9222')
            self.driver = webdriver.Chrome(chrome_options=chrome_opts)
            logging.info("Chrome started!")
        else:
            pass
        self.driver.maximize_window()

    def quit_webdriver(self):
        self.driver.quit()
        logging.info("Browser quit!")

    def find_element(self, element):
        try:
            if element.find_method == 'xpath':
                return self.driver.find_element_by_xpath(element.find_value)
            elif element.find_method == 'class_name':
                return self.driver.find_element_by_class_name(element.find_value)
            elif element.find_method == 'id':
                return self.driver.find_element_by_id(element.find_value)
            elif element.find_method == 'name':
                return self.driver.find_element_by_name(element.find_value)
            elif element.find_method == 'tag_name':
                return self.driver.find_element_by_tag_name(element.find_value)
            elif element.find_method == 'link_text':
                return self.driver.find_element_by_link_text(element.find_value)
            elif element.find_method == 'partial_link_text':
                return self.driver.find_element_by_partial_link_text(element.find_value)
            elif element.find_method == 'css_selector':
                return self.driver.find_element_by_css_selector(element.find_value)
            else:
                logging.error("the find method {find_method}is not correct!".format(find_method=element.find_method))
        except selenium.common.exceptions.NoSuchElementException:
            return None

    def find_elements(self, element):
        try:
            if element.find_method == 'xpath':
                return self.driver.find_elements_by_xpath(element.find_value)
            elif element.find_method == 'class_name':
                return self.driver.find_elements_by_class_name(element.find_value)
            elif element.find_method == 'id':
                return self.driver.find_elements_by_id(element.find_value)
            elif element.find_method == 'name':
                return self.driver.find_elements_by_name(element.find_value)
            elif element.find_method == 'tag_name':
                return self.driver.find_elements_by_tag_name(element.find_value)
            elif element.find_method == 'link_text':
                return self.driver.find_elements_by_link_text(element.find_value)
            elif element.find_method == 'partial_link_text':
                return self.driver.find_elements_by_partial_link_text(element.find_value)
            elif element.find_method == 'css_selector':
                return self.driver.find_elements_by_css_selector(element.find_value)
        except selenium.common.exceptions.NoSuchElementException:
            return None

    def get_url(self, url):
        self.driver.get(url)

    def refresh_page(self):
        self.driver.refresh()
        logging.info("Current page is refreshed!")

    def save_screenshot(self):
        time_str = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        file_name = os.path.join(SCREENSHOOT_PATH, 'screenshot_at_'+ time_str + '.png')
        self.driver.save_screenshot(file_name)
