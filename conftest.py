import pytest
from selenium import webdriver

# Pass args to determine the test environment: prod, dev, or india
# Set to "dev" by default
# ex) "pytest --env prod"
# TODO: Add args for selecting different browsers
def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="dev", help="env options: prod, dev, india"
    )


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def api_url(env):
    if env == "dev":
        return "https://glenis.ywamconverge.org/"  # L10N by Glenis
    elif env == "prod":
        return "https://ywamconverge.org/"  # Prod
    elif env == "india":
        return "https://dev02.ywamconverge.org/"  # India


# Create a fixture as to use a single browser for the session
@pytest.fixture(scope="session")
def browser(request):
    driver = webdriver.Chrome("./chromedriver")
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    driver.maximize_window()
    yield driver
    driver.quit()
