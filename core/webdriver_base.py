from selenium import webdriver
import logging
DOWNLOAD_PATH = ''

class WebDriver:
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
            self.driver = webdriver.Chrome(chrome_options=chrome_opts)
            logging.info("Chrome started!")
        else:
            pass
        self.driver.maximize_window()
        self.driver.set_window_position()

    def quit_webdriver(self):
        self.driver.quit()