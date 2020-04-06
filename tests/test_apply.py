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
                time.sleep(0.05)
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
                    form[headers[4]].replace("email", "email_" + uuid.uuid4().hex),
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

                # Save & Continue to Step 2
                save_xpath = "//form[@id='new_student']//input[@name='commit']"
                self.driver.find_element(By.XPATH, save_xpath).click()

    def test_apply_forms_pg2(self):
        FILE_PATH = "tests/forms/apply_pg2.csv"
        with open(FILE_PATH) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            headers = next(csv_reader)
            for row in csv_reader:
                form = dict(zip(headers, row))

                # Passions
                self.select_when_visible(
                    "//div[@id='s2id_student_application_student_attributes_passions']//ul[@class='select2-choices']",
                    f"//div[contains(text(),'{form[headers[0]]}')]",
                )

                # Highest Education
                self.select_when_visible(
                    "//div[@id='s2id_student_application_student_attributes_overall_education']//a[@class='select2-choice select2-default']",
                    f"//div[contains(text(),'{form[headers[1]]}')]",
                )

                # Graduation Year
                self.select_when_visible(
                    "//div[@id='s2id_student_application_student_attributes_graduation_year']//a[@class='select2-choice select2-default']",
                    f"//div[contains(text(),'{form[headers[2]]}')]",
                )

                # Spoken Languages
                self.select_when_visible(
                    "//div[@id='s2id_student_application_student_attributes_spoken_languages']//ul[@class='select2-choices']",
                    f"//div[contains(text(),'{form[headers[3]]}')]",
                )

                # Fields of Study
                self.select_when_visible(
                    "//div[@id='s2id_student_application_student_attributes_fields_of_study']//ul[@class='select2-choices']",
                    f"//div[contains(text(),'{form[headers[4]]}')]",
                )

                # Cross-Cultural Experiences
                self.select_when_visible(
                    "//div[@id='s2id_student_application_student_attributes_experiences']//ul[@class='select2-choices']",
                    f"//div[contains(text(),'{form[headers[5]]}')]",
                )

                # Tell Us About Yourself
                self.input_text(
                    "//textarea[@id='student_application_student_attributes_description']",
                    form[headers[6]],
                )

                # Spiritual First Name
                self.input_text(
                    "//input[@id='student_application_student_attributes_person_references_attributes_0_contact_first_name']",
                    form[headers[7]],
                )

                # Spiritual Last Name
                self.input_text(
                    "//input[@id='student_application_student_attributes_person_references_attributes_0_contact_last_name']",
                    form[headers[8]],
                )

                # Spiritual Email
                self.input_text(
                    "//input[@id='student_application_student_attributes_person_references_attributes_0_contact_email']",
                    form[headers[9]].replace("email", "email_" + uuid.uuid4().hex),
                )

                # Spiritual Phone
                self.input_text(
                    "//input[@id='student_application_student_attributes_person_references_attributes_0_contact_phone']",
                    form[headers[10]],
                )

                # Spiritual Relationship
                self.input_text(
                    "//input[@id='student_application_student_attributes_person_references_attributes_0_contact_description']",
                    form[headers[11]],
                )

                # Academic First Name
                self.input_text(
                    "//input[@id='student_application_student_attributes_person_references_attributes_1_contact_first_name']",
                    form[headers[12]],
                )

                # Academic Last Name
                self.input_text(
                    "//input[@id='student_application_student_attributes_person_references_attributes_1_contact_last_name']",
                    form[headers[13]],
                )

                # Academic Email
                self.input_text(
                    "//input[@id='student_application_student_attributes_person_references_attributes_1_contact_email']",
                    form[headers[14]].replace("email", "email_" + uuid.uuid4().hex),
                )

                # Academic Phone
                self.input_text(
                    "//input[@id='student_application_student_attributes_person_references_attributes_1_contact_phone']",
                    form[headers[15]],
                )

                # Academic Relationship
                self.input_text(
                    "//input[@id='student_application_student_attributes_person_references_attributes_1_contact_description']",
                    form[headers[16]],
                )

                # Save & Continue to Step 3
                save_xpath = "//form[@class='simple_form edit_student_application']//input[@name='commit']"
                self.driver.find_element(By.XPATH, save_xpath).click()

    def test_apply_forms_pg3(self):
        # Agree to Terms
        checkbox_xpath = "//label[@class='boolean optional control-label checkbox']"
        self.driver.find_element(By.XPATH, checkbox_xpath).click()

        # Save & Continue to Step 4
        save_xpath = "//form[@class='simple_form edit_student_application']//input[@name='commit']"
        self.driver.find_element(By.XPATH, save_xpath).click()

    def test_apply_confirmation_text(self):
        text_xpath = "//div[@class='confirmation']//h2"
        confirmation_text = self.driver.find_element(By.XPATH, text_xpath).text
        assert confirmation_text == "Wahoo, you're all done!"

    # return to homepage via the global variable, CONVERGE_URL, declared in conftest.py
    @pytest.mark.usefixtures("api_url")
    def test_return_to_home(self, api_url):
        self.driver.get(api_url)
