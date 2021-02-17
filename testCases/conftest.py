from selenium import webdriver
import pytest

@pytest.fixture()
# --browser 옵션값을 받아서 브라우저를 지정
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    else:
        driver = webdriver.Ie()
    return driver

# browser option 값 설정
def pytest_addoption(parser):   # This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

##### Pytest HTML Report #####
# It is Hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'SK OPEN API'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'HJH'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)