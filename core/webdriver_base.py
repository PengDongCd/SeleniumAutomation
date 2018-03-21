from selenium import webdriver
import logging
import os

DOWNLOAD_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'outputs/download')
if os.path.exists(DOWNLOAD_PATH):
    os.mkdir(DOWNLOAD_PATH)

class TestWebDriver:
    def __init__(self, browser_name):
        self.browser_name = browser_name

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
            self.driver = webdriver.Chrome(chrome_options=chrome_opts)
            logging.info("Chrome started!")
        else:
            pass
        self.driver.maximize_window()
        return self.driver

    def quit_webdriver(self):
        self.driver.quit()
        logging.info("Browser quit!")