from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.product_list_page import ProductListPage
from pages.shopping_cart_page import ShoppingCartPage
from utils.constants import WEB_URL

class HomePage(BasePage):

    search_box_locator = (By.ID, "ns-search-input")
    search_button_locator = (By.CLASS_NAME, "ns-search-btn")
    cart_icon_locator = (By.XPATH, "//li[contains(@class, 'nav-shopping-cart')]//a")
    cart_badge_locator = (By.CLASS_NAME, "cms-badge")
    header_locator = (By.TAG_NAME, "header")
    
    def __init__(self, driver):
        super().__init__(driver)       

    def open(self):
        self.visit(WEB_URL)
        
    def is_search_box_present(self):
        return self.wait_for_visible(self.search_box_locator)
    
    def enter_search_term(self, term):
        self.type_text(term, *self.search_box_locator)
        return self
    
    def click_search_button(self):
        self.click_element(*self.search_button_locator)
        return ProductListPage(self.driver)
    
    def click_cart_icon(self):
        self.click_element(*self.cart_icon_locator)
        return ShoppingCartPage(self.driver)
        
    def get_cart_badge_amount(self):
        return self.find_element(*self.cart_badge_locator).text