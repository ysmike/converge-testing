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
    # ******************* CUSTOM FUNCTIONS *******************#
    def select_when_visible(self, dropdown_xpath, selection_xpath):
        while True:
            try:
                self.driver.find_element(By.XPATH, dropdown_xpath).click()
                self.driver.find_element(By.XPATH, selection_xpath).click()
                time.sleep(0.5)
            except:
                continue
            return

    def input_text(self, xpath, num):
        self.driver.find_element(By.XPATH, xpath).send_keys(form[headers[num]])

    # ******************* TESTS BEGIN HERE *******************#
    def test_apply_text(self):
        # xpath is indexed from 1, not 0
        link_xpath = "//div[@class='secondary_nav_links']/li[2]"
        apply_link = self.driver.find_element(By.XPATH, link_xpath)
        apply_link.click()
        text_xpath = "//div[@class='new-student-header']/h1"
        header_text = self.driver.find_element(By.XPATH, text_xpath).text
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
                self.driver.find_element(By.XPATH, dropdown_xpath).click()
                selection_xpath = f"//div[contains(text(),'{form[headers[0]]}')]"
                self.driver.find_element(By.XPATH, selection_xpath).click()

                # Your Sessions
                # sleep to load 'Your Sessions' dropdown
                # neither pytest's expected_conditions nor implicitly_wait
                # nor reordering the code toward the bottom worked
                # TODO: consider a while loop continuously clicking & selecting until the wanted field is selected
                # dropdown_xpath = (
                #     "//div[@id='s2id_student_application_project_session_id']"
                # )
                # selection_xpath = f"//div[contains(text(),'{form[headers[1]]}')]"
                self.select_when_visible(
                    "//div[@id='s2id_student_application_project_session_id']",
                    f"//div[contains(text(),'{form[headers[1]]}')]",
                )

                # First Name
                fn_xpath = (
                    "//input[@id='student_application_student_attributes_first_name']"
                )
                fn_el = self.driver.find_element(By.XPATH, fn_xpath)
                fn_el.send_keys(form[headers[2]])

                # Last Name
                ln_xpath = (
                    "//input[@id='student_application_student_attributes_last_name']"
                )
                ln_el = self.driver.find_element(By.XPATH, ln_xpath)
                ln_el.send_keys(form[headers[3]])

                # Email
                email_xpath = "//input[@id='student_application_student_attributes_login_attributes_email']"
                email_el = self.driver.find_element(By.XPATH, email_xpath)
                email = form[headers[4]].replace("email", "email_" + uuid.uuid4().hex)
                email_el.send_keys(email)

                # Password
                pw_xpath = "//input[@id='student_application_student_attributes_login_attributes_password']"
                pw_el = self.driver.find_element(By.XPATH, pw_xpath)
                pw_el.send_keys(form[headers[5]])

                # Password Confirm
                pwc_xpath = "//input[@id='student_application_student_attributes_login_attributes_password_confirmation']"
                pwc_el = self.driver.find_element(By.XPATH, pwc_xpath)
                pwc_el.send_keys(form[headers[6]])

                # Marital Status
                dropdown_xpath = "//div[@id='s2id_student_application_student_attributes_marital_status']//a[@class='select2-choice select2-default']"
                self.driver.find_element(By.XPATH, dropdown_xpath).click()
                selection_xpath = f"//div[contains(text(),'{form[headers[7]]}')]"
                self.driver.find_element(By.XPATH, selection_xpath).click()

                # Birth Year
                dropdown_xpath = "//div[@id='s2id_student_application_student_attributes_birthday_1i']//b"
                self.driver.find_element(By.XPATH, dropdown_xpath).click()
                selection_xpath = f"//div[contains(text(),'{form[headers[8]]}')]"
                self.driver.find_element(By.XPATH, selection_xpath).click()

                # Birth Month
                dropdown_xpath = "//div[@id='s2id_student_application_student_attributes_birthday_2i']//b"
                self.driver.find_element(By.XPATH, dropdown_xpath).click()
                selection_xpath = f"//div[contains(text(),'{form[headers[9]]}')]"
                self.driver.find_element(By.XPATH, selection_xpath).click()

                # Birth Day
                dropdown_xpath = "//div[@id='s2id_student_application_student_attributes_birthday_3i']//b"
                self.driver.find_element(By.XPATH, dropdown_xpath).click()
                selection_xpath = f"//div[contains(text(),'{form[headers[10]]}')]"
                self.driver.find_element(By.XPATH, selection_xpath).click()

                # Gender
                gender_xpath = f"//label[@id='student_application_student_attributes_gender_{form[headers[11]].lower()}']"
                self.driver.find_element(By.XPATH, gender_xpath).click()

                # St Address
                st_xpath = "//input[@id='student_application_student_attributes_street_address']"
                st_el = self.driver.find_element(By.XPATH, st_xpath)
                st_el.send_keys(form[headers[12]])

                # City
                city_xpath = (
                    "//input[@id='student_application_student_attributes_city']"
                )
                city_el = self.driver.find_element(By.XPATH, city_xpath)
                city_el.send_keys(form[headers[13]])

                # State
                state_xpath = (
                    "//input[@id='student_application_student_attributes_state']"
                )
                state_el = self.driver.find_element(By.XPATH, state_xpath)
                state_el.send_keys(form[headers[14]])

                # Postal Code
                postalcode_xpath = (
                    "//input[@id='student_application_student_attributes_postal_code']"
                )
                postalcode_el = self.driver.find_element(By.XPATH, postalcode_xpath)
                postalcode_el.send_keys(form[headers[15]])

                # Country
                dropdown_xpath = "//div[@id='s2id_student_application_student_attributes_country']//a[@class='select2-selection select2-default']"
                self.driver.find_element(By.XPATH, dropdown_xpath).click()
                selection_xpath = f"//div[text()='{form[headers[16]]}']"
                self.driver.find_element(By.XPATH, selection_xpath).click()

                # Preferred Phone
                phone_xpath = "//input[@id='student_application_student_attributes_preferred_phone']"
                phone_el = self.driver.find_element(By.XPATH, phone_xpath)
                phone_el.send_keys(form[headers[17]])

                # Phone Type
                dropdown_xpath = "//div[@id='s2id_student_application_student_attributes_phone_type']//a[@class='select2-selection select2-default']"
                self.driver.find_element(By.XPATH, dropdown_xpath).click()
                selection_xpath = f"//div[contains(text(),'{form[headers[18]]}')]"
                self.driver.find_element(By.XPATH, selection_xpath).click()

                # Organization
                org_xpath = (
                    "//input[@id='student_application_student_attributes_organization']"
                )
                org_el = self.driver.find_element(By.XPATH, org_xpath)
                org_el.send_keys(form[headers[19]])

                # How did you learn about Converge?
                hearfrom_xpath = f"//label[contains(text(), '{form[headers[20]]}')]"
                self.driver.find_element(By.XPATH, hearfrom_xpath).click()

                # Applied Before?
                appliedbefore_xpath = f"//label[text()='{form[headers[21]]}']"
                self.driver.find_element(By.XPATH, appliedbefore_xpath).click()

    # return to homepage via the global variable, CONVERGE_URL, declared in conftest.py
    @pytest.mark.usefixtures("api_url")
    def test_return_to_home(self, api_url):
        self.driver.get(api_url)
