"""
! Prerequisites: Python3, Selenium, Browsers, Browser Drivers
! Make sure to download the drivers for the correct OS & browser version
* Links to the drivers can be found at https://www.selenium.dev/downloads/
? On what OS & browser version will the script run? Issue with Edge driver on MacOS
TODO: Write a shell script to install the above dependencies if needed
"""

import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):
    # use class method to use one instance of the driver for all tests
    @classmethod
    def setUp(cls):
        # create a new Chrome session
        cls.driver = webdriver.Chrome(executable_path='./chromedriver')
        cls.driver.get('https://ywamconverge.org/')
    
    def test_links(self):
