import os
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



class NewVisitorTest(unittest.TestCase):
    
    
    def setUp(self) -> None:
        try:
            os.mkdir('temp')
        except FileExistsError:
            pass

        
        try:
            os.mkdir("temp/driver")
        except FileExistsError:
            pass

        self.driver = webdriver.Chrome(ChromeDriverManager(path="temp/driver").install())


    def tearDown(self) -> None:
        self.driver.quit()

    # ini bagian testing
    def test_start_web(self):
        
        # requests url
        url: str = "http://127.0.0.1:8000/"
        self.driver.get(url)

        # cek html request
        self.assertIn('The install worked successfully! Congratulations!', self.driver.title)



if __name__ == '__main__':
    unittest.main()