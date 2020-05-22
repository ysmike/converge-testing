"""
* Test the text and link interaction on '/support'
"""

import requests

import pytest
from selenium.webdriver.common.by import By

# Set max redirects to 3 from default of 30
r = requests.Session()
r.max_redirects = 3
# Number of seconds before timeout occurs for each request
seconds_to_timeout = 5


@pytest.mark.usefixtures("browser")
class TestDonate:
    # Go to homepage via the global variable declared in conftest.py
    def test_go_to_homepage(self, api_url):
        self.driver.get(api_url)

    def test_donate_text(self, transl):
        donate_text = "nav_donate"
        link_xpath = (
            f"//nav[@class='container']//span[contains(text(),'{transl[donate_text]}')]"
        )
        self.driver.find_element(By.XPATH, link_xpath).click()
        header_xpath = "//article[@class='container']//h2"
        header_text = self.driver.find_element(By.XPATH, header_xpath).text
        assert header_text == transl["support_title"]

    def test_donate_link(self, transl):
        donate_link = "support_general_linktext"
        link_xpath = f"//a[contains(text(),'{transl[donate_link]}')]"
        link_url = self.driver.find_element(By.XPATH, link_xpath).get_attribute("href")
        res = r.get(link_url, timeout=seconds_to_timeout)
        # test status code as DOM elements are not selectable on the final donation page
        assert res.status_code == 200
