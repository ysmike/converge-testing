"""
* Test the text and form interaction on '/projects'
"""

import pytest

from selenium.webdriver.common.by import By


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
        # ! self.driver.back() not necessary when using pytest-xdist
        # ? remove to continue testing on forms?
        self.driver.back()

    def test_internship_forms(self):
        pass

    # return to homepage via the global variable, CONVERGE_URL, in conftest.py
    @pytest.mark.usefixtures("api_url")
    def test_return_to_home(self, api_url):
        self.driver.get(api_url)
