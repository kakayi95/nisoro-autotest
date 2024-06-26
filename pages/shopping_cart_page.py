from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class ShoppingCartPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_item_text(self):
        cart_item = self.find_element(By.CSS_SELECTOR, "[class*='TitleLink']")
        return cart_item.text
   