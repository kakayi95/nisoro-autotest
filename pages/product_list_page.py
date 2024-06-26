from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class ProductListPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def click_first_product(self):
        self.click_element(By.CSS_SELECTOR, ".product-container:first-child a")
        return self.wait_for_element(By.ID, "SalePageIndexController", 10)
   