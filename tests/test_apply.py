"""
* Test the text and form interaction on '/students/setup/about_you'
"""

import csv
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


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

    def test_apply_forms(self):
        FILE_PATH = "tests/forms/apply.csv"
        with open(FILE_PATH) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            headers = next(csv_reader)
            for row in csv_reader:
                form = dict(zip(headers, row))
                # Your Internship
                dropdown_xpath = "//span[@id='select2-chosen-2']"
                self.driver.find_element_by_xpath(dropdown_xpath).click()
                choice_xpath = f"//div[contains(text(),'{form[headers[0]]}')]"
                self.driver.find_element_by_xpath(choice_xpath).click()
                text_xpath = "//div[@class='new-student-header']/h1"
                header_text = self.driver.find_element_by_xpath(text_xpath).click()
                # Your Session
                dropdown_xpath = "//span[contains(text(),'Choose a session')]"
                wait = WebDriverWait(self.driver, 10)
                dropdown = wait.until(
                    ec.visibility_of_element_located(
                        (
                            By.XPATH,
                            "//select[@id='student_application_project_session_id']/option[@value>0]",
                        )
                    )
                )
                dropdown.click()
                self.driver.find_element_by_xpath(dropdown_xpath).click()
                choice_xpath = f"//div[contains(text(),'{form[headers[1]]}')]"
                self.driver.find_element_by_xpath(choice_xpath).click()
                # First Name
                fn_xpath = (
                    "//input[@id='student_application_student_attributes_first_name']"
                )
                fn_el = self.driver.find_element_by_xpath(fn_xpath)
                fn_el.send_keys(form[headers[2]])
