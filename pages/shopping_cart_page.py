from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ShoppingCartPage(BasePage):
    
    item_title_locator = (By.XPATH, "//a[contains(@class, 'TitleLink')]")
    item_price_locator = (By.XPATH, "//div[contains(@class, 'Price')]//div")
    item_amount_locator = (By.XPATH, "//div[contains(@class, 'InputWrpper')]//input[@type='text']")
    layer_container_locator = (By.XPATH, "//div[contains(@class, 'OuterLayer')]")
    products_locator = (By.XPATH, "//div[contains(@class, 'TemperatureGroup')]")
    
    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_item_text(self):
        cart_item = self.find_element(*self.item_title_locator)
        return cart_item.text
   
    def is_loaded(self):
        return self.wait_for_visible(self.layer_container_locator) and \
                self.wait_for_visible(self.item_title_locator) and \
                self.wait_for_visible(self.item_price_locator) and \
                self.wait_for_visible(self.item_amount_locator)
    
    def get_product_amount(self):
        return len(self.find_elements(*self.products_locator))

    def get_item_title(self):
        return self.find_element(*self.item_title_locator).text
    
    def get_item_price(self):
        return self.find_element(*self.item_price_locator).text
    
    def get_item_amount(self):
        return self.find_element(*self.item_amount_locator).get_attribute("value")