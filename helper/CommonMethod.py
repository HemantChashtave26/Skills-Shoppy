from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

from config.testconfig import Testconfig
from testdata.sklogindata import Sklogindata


class Helper:
    driver=None
    def create_driver(self):
        browser=Testconfig.browser_name
        if browser == "chrome":
            self.driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser == "edge":
            self.driver=webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        return self.driver

    def open_url(self):
        self.driver.maximize_window()
        self.driver.get(Testconfig.prod_url)
        time.sleep(5)
        assert self.driver.title == Sklogindata.sk_title

