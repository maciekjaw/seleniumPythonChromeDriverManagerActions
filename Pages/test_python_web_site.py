import unittest
import base

class PythonOrgSearch(base.StartSelenium, unittest.TestCase):
    
    def test_search_in_python_org(self, url:str = "http://www.python.org", expected_word:str = 'Python'):
        driver = self.driver
        driver.get(url)
        self.assertIn(expected_word, driver.title)

if __name__ == "__main__":
    unittest.main()

