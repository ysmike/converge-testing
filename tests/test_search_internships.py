"""
* Test the text and page interaction on '/projects'
"""

import pytest

from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("browser")
class TestSearchInterships:
    def test_go_to_homepage(self, api_url):
        self.driver.get(api_url)

    def test_internship_text(self, transl):
        search_link = self.driver.find_element(
            By.LINK_TEXT, transl["check_out_the_internships"]
        )
        search_link.click()
        filter_text = self.driver.find_element(
            By.XPATH, "//div[@class='filter c3 omega']//div//h3"
        ).text
        filter_details_text = self.driver.find_element(
            By.XPATH, "//div[@id='filter-details']//h4"
        ).text
        assert (
            filter_text == transl["advanced_filters"]
            and filter_details_text == transl["filter_by_passion"]
        )

    # xpath is indexed from 1, not 0
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
        pass
