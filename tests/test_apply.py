"""
* Test the text and form interaction on '/students/setup/about_you'
"""

import pytest


@pytest.mark.usefixtures("browser")
class TestSearchInterships:
    def test_apply(self):
        # xpath is indexed from 1, not 0
        link_xpath = "//div[@class='secondary_nav_links']/li[2]"
        apply_link = self.driver.find_element_by_xpath(link_xpath)
        apply_link.click()
        text_xpath = "//div[@class='new-student-header']/h1"
        header_text = self.driver.find_element_by_xpath(text_xpath).text
        assert header_text == "Student Setup Application"
        # ! self.driver.back() not necessary when using pytest-xdist
        self.driver.back()
