from time import sleep
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#driver_options = webdriver.ChromeOptions()
#driver = webdriver.Chrome()
#driver.get("http://www.python.org")
#assert "Python" in driver.title

google_search_bar_selector:str = "YacQv.gsfi"


class LandingPage(object):
        
        def setUp(self):
                self.driver = webdriver.Chrome(ChromeDriverManager().install())
            #self.driver = webdriver.Chrome()

        def test_search_in_python_org(self):
                driver = self.driver
                driver.get("http://www.python.org")
                self.assertIn("Python", driver.title)

        def tearDown(self):
                self.driver.close()
        
        def search_in_google(searching_word:str):
                google_search_bar = driver.find_element(By.CSS_SELECTOR, google_search_bar_selector).click()
                google_search_bar.send_keys("pycon")
                assert "Python" in driver.title
        
if __name__ == '__main__':
        unittest.main()
        

#landing_page =  LandingPage(driver)
#landing_page.search_in_google("d")

