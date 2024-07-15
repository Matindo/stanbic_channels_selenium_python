### Locators.py ###
# This file will contain the locators: ways in which we locate and identify elements in every page we are testing.
# You can add locators for a page's elements by:
# 1. Skip a single line
# 2. Add the page name as a comment. You can also add the path to the page or url in brackets
# 3. Add all the locators needed for testing

class Locator(object):
    
    # Login Page (https://test-portal.ekenya.co.ke/mobile-banking/auth/login)
    user_input = "//input[@id='email']"
    password_input = "//input[@id='password']"
    login_button = "//button[text()='Login']"