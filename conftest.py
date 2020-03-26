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
    global CONVERGE_URL
    CONVERGE_URL = "https://ywamconverge.org/"
    # CONVERGE_URL = "https://glenis.ywamconverge.org/"  # L10N by Glenis
    # CONVERGE_URL = "https://dev02.ywamconverge.org/"  # India
    driver.get(CONVERGE_URL)  # Current
    driver.maximize_window()
    yield driver
    driver.quit()


# Set global variable to return to homepage
@pytest.fixture(scope="session")
def api_url():
    return CONVERGE_URL
