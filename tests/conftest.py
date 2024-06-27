import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    
@pytest.fixture(scope="module")
def shared_data():
    return {
        "item_name": None,
        "item_price": None,
        "item_amount": None
    }