import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    return webdriver.Chrome(service=service)

# def pytest_configure(config):
#     config._metadata['Project Name'] = 'OrangeHRM'
#     config._metadata['Tester'] = 'Pradeep G'

# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("Plugins", None)
#     metadata.pop("Packages", None)
