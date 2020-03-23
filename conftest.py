"""
* Create a fixture as to use a single browser for the session
"""

import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser(request):
    # TODO: Add args for selecting different/(if possible all) browsers
    driver = webdriver.Chrome("./chromedriver")
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    driver.get("https://ywamconverge.org/")  # Current
    # driver.get("https://glenis.ywamconverge.org/")  # L10N by Glenis
    # driver.get("https://dev02.ywamconverge.org/")  # India
    driver.maximize_window()
    yield driver
    driver.quit()
