import pytest
from selenium import webdriver
from utils.helpers import Helper

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    
@pytest.fixture(scope="module")
def helper(driver):
    return Helper(driver)