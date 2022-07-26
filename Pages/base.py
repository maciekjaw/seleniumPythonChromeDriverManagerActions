import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--remote-debugging-port=9222')

class StartSelenium(unittest.TestCase):
    
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.close()
