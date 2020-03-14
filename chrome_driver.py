"""
! Prerequisites: Python3, Selenium, Requests, Browsers, Browser Drivers
! Make sure to download the drivers for the correct OS & browser version
* Links to the drivers can be found at https://www.selenium.dev/downloads/
? On what OS & browser version will the script run? Issue with Edge driver on MacOS
TODO: Write a shell script to install the above dependencies if needed
"""

# TODO: Add requests to requirements.txt
import requests
import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):
    # use class method to use one driver instance for all tests
    @classmethod
    def setUp(cls):
        # create a new Chrome session
        cls.driver = webdriver.Chrome(executable_path="./chromedriver")
        cls.driver.get("https://ywamconverge.org/")

    def test_for_broken_links(self):
        num_broken_links = 0
        broken_links = {}
        links = [
            link.get_attribute("href")
            for link in self.driver.find_elements_by_tag_name("a")
            if link.get_attribute("href") != "javascript:void(0)"
        ]
        print(f"\nTesting {len(links)} links on the homepage...\n")
        for link in links:
            response = requests.get(link)
            if response.status_code == 200:
                continue
            broken_links[link] = response.status_code
            num_broken_links += 1
        self.assertFalse(
            num_broken_links,
            f"\n{num_broken_links} broken link(s) found:\n{broken_links}",
        )

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
