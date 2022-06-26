from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path


class StartSelenium(object):
    
    def __init__(self, driver) -> None:
        self.driver = driver.Chrome()
        self.driver.get("http://www.google.com")

