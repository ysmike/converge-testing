"""
* Test the status codes of all links on the homepage via 'requerts' module
"""

import requests
import pytest

# Set max redirects to 3 from default of 30
r = requests.Session()
r.max_redirects = 3


@pytest.mark.usefixtures("browser")
class TestLinks:
    def test_status_codes(self):
        num_broken_links = 0
        broken_links = {}
        links = [
            link.get_attribute("href")
            for link in self.driver.find_elements_by_tag_name("a")
            if not link.get_attribute("href").startswith("java")
        ]
        print(f"\nTesting {len(links)} links on the homepage...\n")
        for link in links:
            try:
                res = r.get(link)
                if res.status_code != 200:
                    raise Exception("Status code is not 200")
            except Exception as e:
                # print(link, e, sep=" --> ", end="\n\n") # for debugging
                broken_links[link] = res.status_code
                num_broken_links += 1
        assert (
            num_broken_links == 0
        ), f"\n{num_broken_links} broken link(s) found:\n{broken_links}"
