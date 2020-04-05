"""
* Test the text and form interaction on '/students/setup/about_you'
"""


import csv
import time
import uuid

import pytest

from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("browser")
class TestSearchInterships:
    # ******************* HELPER FUNCTIONS *******************#
    def select_when_visible(self, dropdown_xpath, selection_xpath):
        while True:
            try:
                self.driver.find_element(By.XPATH, dropdown_xpath).click()
                self.driver.find_element(By.XPATH, selection_xpath).click()
                time.sleep(0.2)
            except:
                continue
            return

    def input_text(self, xpath, text):
        self.driver.find_element(By.XPATH, xpath).send_keys(text)

    # ******************* TESTS BEGIN HERE *******************#
    def test_apply_text(self):
        # xpath is indexed from 1, not 0
        link_xpath = "//div[@class='secondary_nav_links']/li[2]"
        apply_link = self.driver.find_element(By.XPATH, link_xpath)
        apply_link.click()
        text_xpath = "//div[@class='new-student-header']/h1"
        header_text = self.driver.find_element(By.XPATH, text_xpath).text
        assert header_text == "Student Setup Application"

    def test_apply_forms_pg1(self):
        FILE_PATH = "tests/forms/apply_pg1.csv"
        with open(FILE_PATH) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            headers = next(csv_reader)
            for row in csv_reader:
                form = dict(zip(headers, row))

                # Your Internship
                self.select_when_visible(
                    "//span[@id='select2-chosen-2']",
                    f"//div[contains(text(),'{form[headers[0]]}')]",
                )

                # Your Sessions
                self.select_when_visible(
                    "//div[@id='s2id_student_application_project_session_id']",
                    f"//div[contains(text(),'{form[headers[1]]}')]",
                )

                # First Name
                self.input_text(
                    "//input[@id='student_application_student_attributes_first_name']",
                    form[headers[2]],
                )

                # Last Name
                self.input_text(
                    "//input[@id='student_application_student_attributes_last_name']",
                    form[headers[3]],
                )

                # Email
                self.input_text(
                    "//input[@id='student_application_student_attributes_login_attributes_email']",
                    form[headers[4]],
                )

                # Password
                self.input_text(
                    "//input[@id='student_application_student_attributes_login_attributes_password']",
                    form[headers[5]],
                )

                # Password Confirm
                self.input_text(
                    "//input[@id='student_application_student_attributes_login_attributes_password_confirmation']",
                    form[headers[6]],
                )

                # Marital Status
                self.select_when_visible(
                    "//div[@id='s2id_student_application_student_attributes_marital_status']//a[@class='select2-choice select2-default']",
                    f"//div[contains(text(),'{form[headers[7]]}')]",
                )

                # Birth Year
                self.select_when_visible(
                    "//div[@id='s2id_student_application_student_attributes_birthday_1i']//b",
                    f"//div[contains(text(),'{form[headers[8]]}')]",
                )

                # Birth Month
                self.select_when_visible(
                    "//div[@id='s2id_student_application_student_attributes_birthday_2i']//b",
                    f"//div[contains(text(),'{form[headers[9]]}')]",
                )

                # Birth Day
                self.select_when_visible(
                    "//div[@id='s2id_student_application_student_attributes_birthday_3i']//b",
                    f"//div[contains(text(),'{form[headers[10]]}')]",
                )

                # Gender
                gender_xpath = (
                    f"//label[contains(text(), '{form[headers[11]].lower()}')]"
                )
                self.driver.find_element(By.XPATH, gender_xpath).click()

                # St Address
                self.input_text(
                    "//input[@id='student_application_student_attributes_street_address']",
                    form[headers[12]],
                )

                # City
                self.input_text(
                    "//input[@id='student_application_student_attributes_city']",
                    form[headers[13]],
                )

                # State
                self.input_text(
                    "//input[@id='student_application_student_attributes_state']",
                    form[headers[14]],
                )

                # Postal Code
                self.input_text(
                    "//input[@id='student_application_student_attributes_postal_code']",
                    form[headers[15]],
                )

                # Country
                self.select_when_visible(
                    "//div[@id='s2id_student_application_student_attributes_country']//a[@class='select2-choice select2-default']",
                    f"//div[text()='{form[headers[16]]}']",
                )

                # Preferred Phone
                self.input_text(
                    "//input[@id='student_application_student_attributes_preferred_phone']",
                    form[headers[17]],
                )

                # Phone Type
                self.select_when_visible(
                    "//div[@id='s2id_student_application_student_attributes_phone_type']//a[@class='select2-choice select2-default']",
                    f"//div[text()='{form[headers[18]]}']",
                )

                # Organization
                self.input_text(
                    "//input[@id='student_application_student_attributes_organization']",
                    form[headers[19]],
                )

                # How did you learn about Converge?
                hearfrom_xpath = f"//label[contains(text(), '{form[headers[20]]}')]"
                self.driver.find_element(By.XPATH, hearfrom_xpath).click()

                # Applied Before?
                appliedbefore_xpath = f"//label[text()='{form[headers[21]]}']"
                self.driver.find_element(By.XPATH, appliedbefore_xpath).click()

    # def test_apply_forms_pg2(self):
    #     FILE_PATH = "tests/forms/apply_pg2.csv"
    #     with open(FILE_PATH) as csv_file:
    #         csv_reader = csv.reader(csv_file, delimiter=",")
    #         headers = next(csv_reader)
    #         for row in csv_reader:
    #             form = dict(zip(headers, row))

    #             # Your Internship
    #             self.select_when_visible(
    #                 "//span[@id='select2-chosen-2']",
    #                 f"//div[contains(text(),'{form[headers[0]]}')]",
    #             )

    #             # Your Sessions
    #             self.select_when_visible(
    #                 "//div[@id='s2id_student_application_project_session_id']",
    #                 f"//div[contains(text(),'{form[headers[1]]}')]",
    #             )

    #             # First Name
    #             self.input_text(
    #                 "//input[@id='student_application_student_attributes_first_name']",
    #                 form[headers[2]],
    #             )

    # return to homepage via the global variable, CONVERGE_URL, declared in conftest.py
    @pytest.mark.usefixtures("api_url")
    def test_return_to_home(self, api_url):
        self.driver.get(api_url)
