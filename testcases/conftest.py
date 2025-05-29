import pytest
from selenium import webdriver

# Command line option for browser
def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Choose browser: chrome or firefox")

# Fetch browser from CLI
@pytest.fixture()
def browser(request):
    return request.config.getoption("browser")

# Browser setup and teardown
@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Browser not supported. Use 'chrome' or 'firefox'.")

    driver.maximize_window()
    yield driver
    driver.quit()

# ----------------- Pytest HTML Report ----------------

# Add custom info to report
def pytest_configure(config):
    if not hasattr(config, '_metadata'):
        config._metadata = {}

    config._metadata['Project Name'] = 'OpCommerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

# Remove unwanted metadata
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



