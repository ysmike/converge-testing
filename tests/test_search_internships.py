"""
* Test the text and form interaction on '/projects'
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
class TestSearchInterships:
    def test_go_to_homepage(self, api_url):
        self.driver.get(api_url)

    def test_internship_text(self):
        search_link = self.driver.find_element(
            By.LINK_TEXT, "Check out the internships"
        )
        search_link.click()
        total_text = self.driver.find_element(By.CLASS_NAME, "total-projects").text[
            -17:
        ]
        filter_text = self.driver.find_element(By.CSS_SELECTOR, ".filter div h3").text
        assert total_text == "Total Internships" and filter_text == "Advanced Filters"

    def test_internship_links(self):
        # num_title_mismatch = 0
        # title_mismatches = {}
        # internships_xpath = (
        #     "//div[@id='related_projects']//div[@class='project-description']/h3"
        # )
        # internships = self.driver.find_elements(By.XPATH, internships_xpath)
        # for internship in internships:
        #     outer_title = internship.text
        #     internship.click()
        #     inner_title = self.driver.find_element(
        #         By.XPATH, "//div[@class='primary']//h1"
        #     ).text
        #     if inner_title != outer_title:
        #         num_title_mismatch += 1
        #         title_mismatches[outer_title] = inner_title
        #     # TODO: Find a workaround to the StaleElementReferenceError (e.g. count cards and loop through using DOM)
        #     self.driver.back()
        # assert (
        #     num_title_mismatch == 0
        # ), f"\n{num_title_mismatch} title mismatch(es) found:\n{title_mismatches}"
