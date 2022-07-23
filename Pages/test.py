
import unittest
import base
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
google_search_bar_selector:str = "YacQv.gsfi"

class PythonOrgSearch(base.StartSelenium, unittest.TestCase):
        
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        
    def test_search_in_google(self):
        google_search_bar = self.driver.find_element(By.CSS_SELECTOR, google_search_bar_selector).click()
        google_search_bar.send_keys("pycon")
        assert "Python" in self.driver.title

if __name__ == "__main__":
    unittest.main()

