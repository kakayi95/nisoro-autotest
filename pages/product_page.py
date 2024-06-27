from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    
    add_to_cart_btn_locator = (By.CLASS_NAME, "add-to-cart-btn")
    product_locator = (By.ID, "SalePageIndexController")
    product_name_locator = (By.CLASS_NAME, "salepage-title")
    quantity_btn_locator = (By.CLASS_NAME, "qty-wrapper")
    immediately_buy_btn_locator = (By.CLASS_NAME, "immediately-buy-btn")
    add_to_cart_success_locator = (By.XPATH, "//span[@data-qe-id='popup_msg' and contains(text(), '加入成功')]")

    def __init__(self, driver):
        super().__init__(driver)
        
    def is_loaded(self):
        return self.wait_for_visible(self.product_locator, 30) 
    
    def get_product_title(self):
        return self.find_element(*self.product_name_locator).text
    
    def is_add_to_cart_button_clickable(self):
        return self.wait_for_clickable(self.add_to_cart_btn_locator)
        
    def is_quantity_button_present(self):
        return self.is_element_present(*self.quantity_btn_locator)
    
    def is_add_to_cart_button_present(self):
        return self.is_element_present(*self.add_to_cart_btn_locator)
    
    def is_immediately_buy_button_present(self):
        return self.is_element_present(*self.immediately_buy_btn_locator)
    
    def add_to_cart(self, quantity=1):
        self.click_element(*self.add_to_cart_btn_locator)
        
