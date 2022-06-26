from time import sleep
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from start import StartSelenium 
import unittest


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver_options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
#driver.get("http://www.python.org")
#assert "Python" in driver.title

google_search_bar_selector:str = "YacQv.gsfi"


class LandingPage(StartSelenium,unittest.TestCase):
            
    def search_in_google(searching_word:str):
        google_search_bar = driver.find_element(By.CSS_SELECTOR, google_search_bar_selector).click()
        google_search_bar.send_keys("pycon")
        assert "Python" in driver.title
        
if __name__ == '__main__':
        unittest.main()
        

#landing_page =  LandingPage(driver)
#landing_page.search_in_google("d")

