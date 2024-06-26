from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        self.driver.get(url)

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        
    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def click_element(self, by, value):
        element = self.find_element(by, value)
        element.click()
        
    def send_keys(self, by, value, key):
        element = self.find_element(by, value)
        element.send_keys(key)