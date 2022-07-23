import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class StartSelenium(unittest.TestCase):
    
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://www.google.com")
    
    def tearDown(self):
        self.driver.close()
