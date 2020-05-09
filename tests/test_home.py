"""
* Test the status codes of all links on the homepage via 'requests' module
"""

import requests
import pytest

from selenium.webdriver.common.by import By

# Set max redirects to 3 from default of 30
r = requests.Session()
r.max_redirects = 3
# Number of seconds before timeout occurs for each request
seconds_to_timeout = 5


@pytest.mark.usefixtures("browser")
class TestLinks:
    def test_go_to_homepage(self, api_url):
        self.driver.get(api_url)

    def test_status_codes(self):
        num_broken_links = 0
        broken_links = {}
        links = [
            link.get_attribute("href")
            for link in self.driver.find_elements(By.TAG_NAME, "a")
            if not link.get_attribute("href").startswith("java")
        ]
        print(f"\nTesting {len(links)} links on the homepage...\n")
        for link in links:
            try:
                res = r.get(link, timeout=seconds_to_timeout)
                if res.status_code != 200:
                    raise Exception("Status code is not 200")
            except Exception as e:
                # print(link, e, sep=" --> ", end="\n\n") # for debugging
                broken_links[link] = res.status_code
                num_broken_links += 1
        assert (
            num_broken_links == 0
        ), f"\n{num_broken_links} broken link(s) found:\n{broken_links}"
