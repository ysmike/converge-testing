"""
* Test the text and form interaction on '/projects'
"""

import pytest


@pytest.mark.usefixtures("browser")
class TestSearchInterships:
    def test_texts(self):
        search_link = self.driver.find_element_by_link_text("Check out the internships")
        search_link.click()
        total_text = self.driver.find_element_by_class_name("total-projects").text[-17:]
        filter_text = self.driver.find_element_by_css_selector(".filter div h3").text
        assert total_text == "Total Internships" and filter_text == "Advanced Filters"
        # ! self.driver.back() not necessary when using pytest-xdist
        self.driver.back()
