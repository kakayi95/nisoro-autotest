from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.constants import BASE_URL

class HomePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = BASE_URL
        self.search_input_id = "ns-search-input"

    def open(self):
        self.visit(self.url)

    def search_product(self, product_name):
        self.send_keys(By.ID, self.search_input_id, product_name)
        self.send_keys(By.ID, self.search_input_id, Keys.RETURN)
        return self.wait_for_element(By.CLASS_NAME, "product-container", 10)
    
    def click_cart_icon(self):
        self.click_element(By.CLASS_NAME, "nav-shopping-cart")
        return self.wait_for_element(By.CSS_SELECTOR, "[class*='TitleLink']", 10)
   