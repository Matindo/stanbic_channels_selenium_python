### Open Login Page Test Script ###

# setup paths for reference
import sys
import os
sys.path.append(os.getcwd())
# imports of files and functions
from Src.TestBase.ChromeWebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.LoginPage import Login
import unittest
from time import sleep

class Stanchart_Login_Page(WebDriverSetup):
    
    def test_login_Page(self):
        driver = self.driver
        self.driver.get("https://test-portal.ekenya.co.ke/mobile-banking/auth/login")
        self.driver.set_page_load_timeout(30)
        
        web_page_title = "Mobile Banking"
        # check page load
        try:
            if driver.title == web_page_title:
                print("Successful Page Load")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "Failed Page Load")
              
        sleep(5)
        
if __name__ == '__main__':
    unittest.main()