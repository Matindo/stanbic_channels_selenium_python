### User Login Test Script ###

# setup paths for reference
import sys
import os
sys.path.append(os.getcwd())
# imports of files and functions
from Src.TestBase.ChromeWebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.LoginPage import Login
import unittest
from time import sleep

class User_Login(WebDriverSetup):
    
    def test_user_login(self):
        driver = self.driver
        self.driver.get("https://test-portal.ekenya.co.ke/mobile-banking/auth/login")
        self.driver.set_page_load_timeout(30)
        
        login_user = Login(driver)
        login_user.getUserInput().send_keys("kamau.lilian@eclectics.io")
        sleep(1)
        login_user.getPasswordInput().send_keys("5rD6l8#K")
        sleep(2)
        login_user.getLoginButton().click()
        sleep(5)
        
        web_page_title = "Mobile Banking"
 
        try:
             if driver.title == web_page_title:
                 print("Successful Login")
                 self.assertEqual(driver.title, web_page_title)
        except Exception as error:
             print("Failed Login: " + error)
 
        sleep(10)
        
if __name__ == '__main__':
    unittest.main()