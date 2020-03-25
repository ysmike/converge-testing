"""
* Test the text and form interaction on '/students/setup/about_you'
"""

import csv
import time
import uuid

import pytest


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
                
                # Your Sessions
                # sleep to load 'Your Sessions' dropdown
                # neither pytest's expected_conditions nor implicitly_wait
                # nor reordering the code toward the bottom worked
                time.sleep(7)
                dropdown_id = 's2id_student_application_project_session_id'
                self.driver.find_element_by_id(dropdown_id).click()
                choice_xpath = f"//div[contains(text(),'{form[headers[1]]}')]"
                self.driver.find_element_by_xpath(choice_xpath).click()
                
                # First Name
                fn_xpath = (
                    "//input[@id='student_application_student_attributes_first_name']"
                )
                fn_el = self.driver.find_element_by_xpath(fn_xpath)
                fn_el.send_keys(form[headers[2]])
                
                # Last Name
                ln_xpath = (
                    "//input[@id='student_application_student_attributes_last_name']"
                )
                ln_el = self.driver.find_element_by_xpath(ln_xpath)
                ln_el.send_keys(form[headers[3]])

                # Email
                email_xpath = (
                    "//input[@id='student_application_student_attributes_login_attributes_email']"
                )
                email_el = self.driver.find_element_by_xpath(email_xpath)
                email = form[headers[4]].replace('email', 'email_' + uuid.uuid4().hex)
                email_el.send_keys(email)
                
                # Password
                pw_xpath = (
                    "//input[@id='student_application_student_attributes_login_attributes_password']"
                )
                pw_el = self.driver.find_element_by_xpath(pw_xpath)
                pw_el.send_keys(form[headers[5]])
                
                # Password Confirm
                pwc_xpath = (
                    "//input[@id='student_application_student_attributes_login_attributes_password_confirmation']"
                )
                pwc_el = self.driver.find_element_by_xpath(pwc_xpath)
                pwc_el.send_keys(form[headers[6]])

                

    
        
        
