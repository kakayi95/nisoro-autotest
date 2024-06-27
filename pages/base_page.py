from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        self.driver.get(url)

    def wait_for_presence(self, loc, timeout = 10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(loc)
            )
            return True
        except TimeoutException:
            return False
        
    def wait_for_visible(self, loc, timeout = 10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(loc)
            )
            return True
        except TimeoutException:
            return False
        
    def wait_for_invisible(self, loc, timeout = 10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(loc)
            )
            return True
        except TimeoutException:
            return False
        
    def wait_for_clickable(self, loc, timeout = 10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(loc)
            )
            return True
        except TimeoutException:
            return False

    def click_element(self, *loc):
        element = self.find_element(*loc)
        element.click()
    
    def type_text(self, text, *loc):
       self.find_element(*loc).send_keys(text)
        
    def find_element(self, *loc):
       return self.driver.find_element(*loc)
   
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)
       
    def is_element_present(self, *loc):
        try:
            self.find_element(*loc)
            return True
        except NoSuchElementException:
            return False