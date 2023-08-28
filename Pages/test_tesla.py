import unittest
import base
from selenium.webdriver.common.by import By

SHOP_BTN:str = "tds-btn tds-btn--tertiary"

class Tesla(base.StartSelenium, unittest.TestCase):
        
        def test_go_to_tesla_shop(self, url:str = "https://www.tesla.com",expected_url:str = 'https://shop.tesla.com'):    
        
                driver = self.driver
                driver.get(url)
                driver.find_element(By.CLASS_NAME, SHOP_BTN).click()
                get_shop_url = driver.current_url
                self.assertNotEqual(get_shop_url, expected_url)
        
if __name__ == "__main__":
    unittest.main()
