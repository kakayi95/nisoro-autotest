from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class ProductPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def add_to_cart(self):
        self.click_element(By.CLASS_NAME, "add-to-cart-btn")

   