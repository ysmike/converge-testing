import pytest
import selenium
import yaml

# Use a single browser for the whole session
@pytest.fixture(scope="session")
def browser(request, browserdriver):
    # Keep commands as string to avoid spinning up instances of all browsers
    drivers = {
        "chrome": "selenium.webdriver.Chrome()",
        "safari": "selenium.webdriver.Safari()",
        "firefox": "selenium.webdriver.Firefox()",
        # "edge": "selenium.webdriver.Edge()", # requires an 'MicrosoftWebDriver.exe' per error
    }
    driver = eval(drivers.get(browserdriver))
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    driver.maximize_window()
    yield driver
    driver.quit()


# Command line argument options:
# --env prod | dev | india
# --locale en | es
# --browserdriver chrome | edge | firefox
def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="prod", help="env options: prod, dev, india"
    )
    parser.addoption(
        "--locale", action="store", default="en", help="locale options: en, es"
    )
    parser.addoption(
        "--browserdriver",
        action="store",
        default="chrome",
        help="browserdriver options: chrome, edge, firefox",
    )


# store the environment input in the "env" fixture
@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


# store the locale input in the "locale" fixture
@pytest.fixture(scope="session")
def locale(request):
    return request.config.getoption("--locale")


# store the locale input in the "browserdriver" fixture
@pytest.fixture(scope="session")
def browserdriver(request):
    return request.config.getoption("--browserdriver")


# set "api_url" as a fixture that can be passed as an argument in tests
@pytest.fixture(scope="session")
def api_url(env, locale):
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
