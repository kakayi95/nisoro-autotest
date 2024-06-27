from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.product_page import ProductPage

class ProductListPage(BasePage):
    
    product_list_locator = (By.CLASS_NAME, "product-container")
    product_item_locator = (By.CLASS_NAME, "new-product-card")
    product_name_locator = (By.XPATH, "//a[contains(@class, 'new-product-card')]/div/div[2]/div/div")
    
    def __init__(self, driver):
        super().__init__(driver)
       
    def is_loaded(self):
        return self.wait_for_visible(self.product_list_locator)
    
    def has_products(self):
        return len(self.find_elements(*self.product_item_locator)) > 0
    
    def get_first_product(self):
        return self.find_element(*self.product_item_locator)
    
    def get_first_product_title(self):
        return self.find_element(*self.product_name_locator).text
    
    def click_first_product(self):
        self.click_element(*self.product_item_locator)
        return ProductPage(self.driver)
        
    def contain_term(self, product_text, term):
        return term in product_text