import pytest
import selenium
import yaml

# Use a single browser for the whole session
@pytest.fixture(scope="session")
def browser(request):
    driver = selenium.webdriver.Chrome("./chromedriver")
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    driver.maximize_window()
    yield driver
    driver.quit()


# pass args to determine the testing environment: prod, dev, or india
# set to "prod" by default
# ex) "pytest --env dev"
# pass args to determine the testing lcoale: en or es
# set to "en" by default
# ex) "pytest --locale es"
# TODO: Add args for selecting different browsers
# TODO: consolidate comments for command line options (browser, locale, environment)
def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="prod", help="env options: prod, dev, india"
    )
    parser.addoption(
        "--locale", action="store", default="en", help="locale options: en, es"
    )


# store the environment input in the "env" fixture
@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


# store the locale input in the "locale" fixture
@pytest.fixture(scope="session")
def locale(request):
    return request.config.getoption("--locale")


# set "api_url" as a fixture that can be passed as an argument in tests
@pytest.fixture(scope="session")
def api_url(env, locale):
    # don't append locale to url if it is English
    locale = "" if locale == "en" else locale
    if env == "dev":
        return f"https://glenis.ywamconverge.org/{locale}"  # L10N by Glenis
    elif env == "prod":
        return f"https://ywamconverge.org/{locale}"  # Prod
    elif env == "india":
        return f"https://dev02.ywamconverge.org/{locale}"  # India


@pytest.fixture(scope="session")
def transl(locale):
    with open(f"localization/{locale}.yml") as transl:
        data = yaml.safe_load(transl)
    return data[f"{locale}"]
