"""
* Test the text and form interaction on '/projects/setup/about_you'
"""


import csv
import time
import uuid

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("browser")
class TestSearchInterships:
    # ******************* HELPER FUNCTIONS ******************* #
    def select_when_visible(
        self,
        dropdown_xpath,
        selection_xpath="//div[starts-with(@id, 'select2-result-label-')]",
    ):
        while True:
            try:
                self.driver.find_element(By.XPATH, dropdown_xpath).click()
                self.driver.find_element(By.XPATH, selection_xpath).click()
                time.sleep(0.05)
            except:
                continue
            return

    def input_text(self, xpath, text):
        self.driver.find_element(By.XPATH, xpath).send_keys(text)

    # ******************* TESTS BEGIN HERE ******************* #
    # Go to homepage via the global variable declared in conftest.py
    def test_go_to_homepage(self, api_url):
        self.driver.get(api_url)

    def test_create_text(self, transl):
        # xpath is indexed from 1, not 0
        link_xpath = "//div[@class='secondary_nav_links']/li[1]"
        self.driver.find_element(By.XPATH, link_xpath).click()
        text_xpath = "//h1[@class='center']"
        header_text = self.driver.find_element(By.XPATH, text_xpath).text
        assert header_text == transl["project_setup_application"]

    def test_create_forms_pg1(self):
        FILE_PATH = "forms/create_pg1.csv"
        with open(FILE_PATH) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            headers, row = next(csv_reader), next(csv_reader)
            form = dict(zip(headers, row))

        # Salutation
        self.select_when_visible(
            "//div[@id='s2id_project_field_host_attributes_salutation']//a"
        )

        # First Name (Nick name)
        self.input_text(
            "//input[@id='project_field_host_attributes_first_name']", form[headers[0]]
        )

        # Initial
        self.input_text(
            "//input[@id='project_field_host_attributes_middle_initial']",
            form[headers[1]],
        )

        # Last Name
        self.input_text(
            "//input[@id='project_field_host_attributes_last_name']", form[headers[2]]
        )

        # Email
        self.input_text(
            "//input[@id='project_field_host_attributes_login_attributes_email']",
            form[headers[3]].replace("email", "email_" + uuid.uuid4().hex),
        )

        # Password
        self.input_text(
            "//input[@id='project_field_host_attributes_login_attributes_password']",
            form[headers[4]],
        )

        # Password Confirm
        self.input_text(
            "//input[@id='project_field_host_attributes_login_attributes_password_confirmation']",
            form[headers[5]],
        )

        # Preferred Phone
        self.input_text(
            "//input[@id='project_field_host_attributes_preferred_phone']",
            form[headers[6]],
        )

        # Phone Type
        self.select_when_visible(
            "//div[@id='s2id_project_field_host_attributes_phone_type']//a"
        )

        # Existing Organization
        self.select_when_visible(
            "//div[@id='s2id_project_organization_id']//a[@class='select2-choice select2-default']"
        )

        # Role Title
        self.input_text(
            "//input[@id='project_field_host_attributes_role_title']", form[headers[7]]
        )

        # Years Associated with Organization
        self.input_text(
            "//input[@id='project_field_host_attributes_years_associated_with_organization']",
            form[headers[8]],
        )

        # Overall Education
        self.select_when_visible(
            "//div[@id='s2id_project_field_host_attributes_overall_education']//a"
        )

        # What has your experience been with YWAM?
        dts_xpath = "//label[@for='project_field_host_attributes_experience_with_ywam_ywam_dts']"
        self.driver.find_element(By.XPATH, dts_xpath).click()

        # How did you learn about Converge?
        hearfrom_ywam_xpath = (
            "//label[@for='project_field_host_attributes_heard_about_ipo_ywam_staff']"
        )
        hearfrom_event_xpath = (
            "//label[@for='project_field_host_attributes_heard_about_ipo_event']"
        )
        self.driver.find_element(By.XPATH, hearfrom_ywam_xpath).click()
        self.driver.find_element(By.XPATH, hearfrom_event_xpath).click()

        # Contact First Name
        self.input_text(
            "//input[@id='project_field_host_attributes_person_references_attributes_0_contact_first_name']",
            form[headers[9]],
        )

        # Contact Last Name
        self.input_text(
            "//input[@id='project_field_host_attributes_person_references_attributes_0_contact_last_name']",
            form[headers[10]],
        )

        # Contact Email
        self.input_text(
            "//input[@id='project_field_host_attributes_person_references_attributes_0_contact_email']",
            form[headers[11]].replace("email", "email_" + uuid.uuid4().hex),
        )

        # Contact Phone
        self.input_text(
            "//input[@id='project_field_host_attributes_person_references_attributes_0_contact_phone']",
            form[headers[12]],
        )

        # How did you know this person?
        self.input_text(
            "//input[@id='project_field_host_attributes_person_references_attributes_0_contact_description']",
            form[headers[13]],
        )

        # Save & Continue to Step 2
        save_xpath = "//form[@id='new_project']//input[@name='commit']"
        self.driver.find_element(By.XPATH, save_xpath).click()
        time.sleep(5)

    # def test_create_forms_pg2(self):
    #     FILE_PATH = "forms/create_pg2.csv"
    #     with open(FILE_PATH) as csv_file:
    #         csv_reader = csv.reader(csv_file, delimiter=",")
    #         headers = next(csv_reader)
    #         row = next(csv_reader)
    #         form = dict(zip(headers, row))

    #     # Passions
    #     self.select_when_visible(
    #         "//div[@id='s2id_student_application_student_attributes_passions']//ul[@class='select2-choices']"
    #     )

    #     # Highest Education
    #     self.select_when_visible(
    #         "//div[@id='s2id_student_application_student_attributes_overall_education']//a[@class='select2-choice select2-default']"
    #     )

    #     # Graduation Year
    #     self.select_when_visible(
    #         "//div[@id='s2id_student_application_student_attributes_graduation_year']//a[@class='select2-choice select2-default']"
    #     )

    #     # Spoken Languages
    #     self.select_when_visible(
    #         "//div[@id='s2id_student_application_student_attributes_spoken_languages']//ul[@class='select2-choices']"
    #     )

    #     # Fields of Study
    #     self.select_when_visible(
    #         "//div[@id='s2id_student_application_student_attributes_fields_of_study']//ul[@class='select2-choices']"
    #     )

    #     # Cross-Cultural Experiences
    #     self.select_when_visible(
    #         "//div[@id='s2id_student_application_student_attributes_experiences']//ul[@class='select2-choices']"
    #     )

    #     # Tell Us About Yourself
    #     self.input_text(
    #         "//textarea[@id='student_application_student_attributes_description']",
    #         form[headers[6]],
    #     )

    #     # Spiritual First Name
    #     self.input_text(
    #         "//input[@id='student_application_student_attributes_person_references_attributes_0_contact_first_name']",
    #         form[headers[7]],
    #     )

    #     # Spiritual Last Name
    #     self.input_text(
    #         "//input[@id='student_application_student_attributes_person_references_attributes_0_contact_last_name']",
    #         form[headers[8]],
    #     )

    #     # Spiritual Email
    #     self.input_text(
    #         "//input[@id='student_application_student_attributes_person_references_attributes_0_contact_email']",
    #         form[headers[9]].replace("email", "email_" + uuid.uuid4().hex),
    #     )

    #     # Spiritual Phone
    #     self.input_text(
    #         "//input[@id='student_application_student_attributes_person_references_attributes_0_contact_phone']",
    #         form[headers[10]],
    #     )

    #     # Spiritual Relationship
    #     self.input_text(
    #         "//input[@id='student_application_student_attributes_person_references_attributes_0_contact_description']",
    #         form[headers[11]],
    #     )

    #     # Academic First Name
    #     self.input_text(
    #         "//input[@id='student_application_student_attributes_person_references_attributes_1_contact_first_name']",
    #         form[headers[12]],
    #     )

    #     # Academic Last Name
    #     self.input_text(
    #         "//input[@id='student_application_student_attributes_person_references_attributes_1_contact_last_name']",
    #         form[headers[13]],
    #     )

    #     # Academic Email
    #     self.input_text(
    #         "//input[@id='student_application_student_attributes_person_references_attributes_1_contact_email']",
    #         form[headers[14]].replace("email", "email_" + uuid.uuid4().hex),
    #     )

    #     # Academic Phone
    #     self.input_text(
    #         "//input[@id='student_application_student_attributes_person_references_attributes_1_contact_phone']",
    #         form[headers[15]],
    #     )

    #     # Academic Relationship
    #     self.input_text(
    #         "//input[@id='student_application_student_attributes_person_references_attributes_1_contact_description']",
    #         form[headers[16]],
    #     )

    #     # Save & Continue to Step 3
    #     save_xpath = "//form[@class='simple_form edit_student_application']//input[@name='commit']"
    #     self.driver.find_element(By.XPATH, save_xpath).click()

    # def test_create_forms_pg3(self):
    #     # Agree to Terms
    #     checkbox_xpath = "//label[@class='boolean optional control-label checkbox']"
    #     self.driver.find_element(By.XPATH, checkbox_xpath).click()

    #     # Save & Continue to Step 4
    #     save_xpath = "//form[@class='simple_form edit_student_application']//input[@name='commit']"
    #     self.driver.find_element(By.XPATH, save_xpath).click()

    # def test_create_confirmation_text(self, transl):
    #     text_xpath = "//div[@class='confirmation']//h2"
    #     confirmation_text = self.driver.find_element(By.XPATH, text_xpath).text
    #     assert confirmation_text == transl["submission_confirmation"]
