"""
* Test the text and page interaction on '/projects'
"""

import pytest

from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("browser")
class TestSearch:
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

    def test_internship_links(self):
        num_title_mismatch, title_mismatches = 0, {}
        internships = self.driver.find_elements(
            By.XPATH, "//div[@id='related_projects']//a"
        )
        # xpath is indexed from 1, not 0
        for int_num in range(1, len(internships) + 1):
            internship_xpath = f"//div[@id='related_projects']//a[{int_num}]//div[@class='project-description']//h3"
            internship = self.driver.find_element(By.XPATH, internship_xpath)
            outer_title = internship.text
            internship.click()
            inner_title_xpath = "//div[@class='primary']//h1"
            inner_title = self.driver.find_element(By.XPATH, inner_title_xpath).text
            if inner_title != outer_title:
                num_title_mismatch += 1
                title_mismatches[outer_title] = inner_title
            self.driver.back()
        assert_str = (
            f"\n{num_title_mismatch} title mismatch(es) found:\n{title_mismatches}"
        )
        assert num_title_mismatch == 0, assert_string
