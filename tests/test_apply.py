"""
* Test the text and form interaction on '/students/setup/about_you'
"""

import csv
import pytest
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures("browser")
class TestSearchInterships:
    def test_apply_text(self):
        # xpath is indexed from 1, not 0
        link_xpath = "//div[@class='secondary_nav_links']/li[2]"
        apply_link = self.driver.find_element_by_xpath(link_xpath)
        apply_link.click()
        text_xpath = "//div[@class='new-student-header']/h1"
        header_text = self.driver.find_element_by_xpath(text_xpath).text
        assert header_text == "Student Setup Application"
        # ! self.driver.back() not necessary when using pytest-xdist
        # ? remove to continue testing on forms?
        self.driver.back()

    def test_apply_forms(self):
        FILE_PATH = "forms/apply.csv"
        with open(FILE_PATH) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            headers = next(csv_reader)
            for row in csv_reader:
                form = dict(zip(headers, row))
                # ? select each form by xpath or use tab to complete?
                int_xpath = "//select[@name='your_project_select']"
                int_sel = Select(self.driver.find_element_by_xpath(int_xpath))
                int_sel.select_by_visible_text(form[header[0]])
                # int_sel.select_by_value('348')
                # int_sel.select_by_index(2)

                sess_xpath = "//select[@name='student_application[project_session_id]']"
                sess_sel = Select(self.driver.find_element_by_xpath(sess_xpath))
                int_sel.select_by_visible_text(
                    "Ruby on Rails, Mobile, or Salesforce Tech"
                )
