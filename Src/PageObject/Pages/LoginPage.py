### Stanchart Channels Login Page ###

# setup paths for reference
import sys
import os
sys.path.append(os.getcwd())
# imports of files and functions
from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Locator

class Login(object):
    def __init__(self, driver):
        self.driver = driver
        self.user_input = driver.find_element(By.XPATH, Locator.user_input)
        self.password_input = driver.find_element(By.XPATH, Locator.password_input)
        self.login_button = driver.find_element(By.XPATH, Locator.login_button)
        
    def getLoginButton(self):
        return self.login_button
    
    def getUserInput(self):
        return self.user_input
    
    def getPasswordInput(self):
        return self.password_input