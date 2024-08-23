import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key


def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",
                     help="Specify the browser: chrome or firefox or Edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "Edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")
    return driver


########## for pytest html reports  ##########
###### Hook for adding environment info in HTML report ########
def pytest_configure(config):
    config.stash[metadata_key] ['project Name'] = 'Ecommerce Project, nopcommerce'
    config.stash[metadata_key]['Test Module Name'] = 'Admin Login Tests'
    config.stash[metadata_key]['Tester Name'] = 'Nitesh'

### Hook for delete/modify environment info in HTML report
# @pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins',None)


