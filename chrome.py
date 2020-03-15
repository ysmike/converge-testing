"""
! Prerequisites: Python3, Selenium, Requests, Browsers, Browser Drivers
! Make sure to download the drivers for the correct OS & browser version
* Links to the drivers can be found at https://www.selenium.dev/downloads
? On what OS & browser version will the script run? Issue with Edge driver on MacOS
? Should I write a shell script to install the above dependencies?
# flake8 ywam.py --ignore E501
"""

import requests
import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):
    # implement class method to use one driver instance for all tests
    @classmethod
    def setUpClass(cls):
        # TODO: Add a file for MS Edge and use TestSuite to combine the two
        cls.driver = webdriver.Chrome(executable_path="chromedriver")
        # maximize window to expand the hamburger menu
        cls.driver.maximize_window()
        cls.driver.get("https://ywamconverge.org/")

    def test_status_code(self):
        "Validate all hyperlinks on the homepage via the requests module"
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

    def test_search_internships(self):
        "Click on 'Search Interships' and validate strings"
        print("\nTesting search internships...\n")
        search_link = self.driver.find_element_by_link_text("Check out the internships")
        search_link.click()
        total_text = self.driver.find_element_by_class_name("total-projects").text[-17:]
        self.assertEqual("Total Internships", total_text)
        filter_text = self.driver.find_element_by_css_selector(".filter div h3").text
        self.assertEqual("Advanced Filters", filter_text)
        self.driver.back()

    def test_apply(self):
        "Click on 'donate' and validate strings"
        print("\nTesting apply...\n")
        apply_link = self.driver.find_element_by_xpath(
            # XPath is indexed from 1, not 0
            "//div[@class='secondary_nav_links']/li[2]"
        )
        apply_link.click()
        header_text = self.driver.find_element_by_xpath(
            "//div[@class='new-student-header']/h1"
        ).text
        self.assertEqual("Student Setup Application", header_text)
        self.driver.back()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
