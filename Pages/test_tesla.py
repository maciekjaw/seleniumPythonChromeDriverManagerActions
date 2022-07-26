import unittest
import base
from selenium.webdriver.common.by import By

class LandingPage(base.StartSelenium, unittest.TestCase):
        
        def test_go_to_tesla_shop(self, url:str = "https://www.tesla.com", expected_word:str = 'https://shop.tesla.com'):
                driver = self.driver
                driver.get(url)
                driver.find_element(By.CLASS_NAME, "tds-site-nav-item-text").click()
                self.assertIn(expected_word, driver.current_url)
        
if __name__ == '__main__':
        unittest.main()


