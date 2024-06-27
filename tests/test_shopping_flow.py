from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from pages.product_page import ProductPage
from pages.shopping_cart_page import ShoppingCartPage
from utils.constants import *


class TestShoppingFlow:
    
    search_term = "花椰菜米"
        
    def test_open_website(self, driver):
        """
        Test to open the target website.
        """
        home_page = HomePage(driver)
        home_page.open()
        
        # Check the homepage title
        expected_title = WEB_TITLE
        assert expected_title in driver.title, f"Title mismatch: expected '{expected_title}', got '{driver.title}'"

    def test_search_box_present(self, driver):
        """
        Test to verify that the search box is present on the home page.
        """
        # Wait for search box to load
        home_page = HomePage(driver)  
    
        # Check if search box is present
        assert home_page.wait_for_visible(home_page.search_box_locator), "Search box not found"

    def test_search_for_product(self, driver):
        """
        Test to search for a product by entering a search query and submitting it.
        """
        home_page = HomePage(driver)
        product_list_page = home_page.enter_search_term(self.search_term).click_search_button()
        
        # Check if product list page is loaded
        assert product_list_page.is_loaded(), "Product list page not loaded"
        # Check if there are products in the search results
        assert product_list_page.has_products(), "No products found in search results"
        
    def test_first_product_information(self, driver):
        product_list_page = ProductListPage(driver)
        # Check if the first product exists and is clickable
        first_product_name = product_list_page.get_first_product_title()
  
        assert product_list_page.contain_term(first_product_name, self.search_term), f"First product does not contain search term '{self.search_term}', but got '{first_product_name}'"
        assert product_list_page.wait_for_clickable(product_list_page.product_item_locator), "First product is not clickable"

    def test_open_product_page(self, driver):
        """
        1. Test to open the first product's detail page from the search results.
        2. Waits for the product detail page to load and verifies its presence.
        """
    
        product_list_page = ProductListPage(driver)
        expected_product_name = product_list_page.get_first_product_title()
        
        product_page = product_list_page.click_first_product()
        actual_product_name = product_page.get_product_title()
        
        assert product_page.is_loaded(), "Failed to open product detail page"
        assert expected_product_name == actual_product_name, "Product name mismatch"
        
    def test_product_is_available(self, driver):
        product_page = ProductPage(driver)
        assert product_page.is_quantity_button_present(), "Quantity button not found"
        assert product_page.is_add_to_cart_button_present() and product_page.is_add_to_cart_button_clickable(), "Add to cart button not usable"
        assert product_page.is_immediately_buy_button_present(), "Buy now button not usable"

    def test_add_product_to_cart(self, driver):
        """
        Test to add the product to the shopping cart.
        """
        product_page = ProductPage(driver)
        product_page.add_to_cart()
        
        assert product_page.wait_for_visible(product_page.add_to_cart_success_locator), "Failed to add product to cart"
        assert product_page.wait_for_invisible(product_page.add_to_cart_success_locator), "Failed to close modal"
        assert HomePage(driver).get_cart_badge_amount() == "1", "Failed to add product to cart"
        
    def test_open_shopping_cart_page(self, driver):
        home_page = HomePage(driver)
        shopping_cart_page = home_page.click_cart_icon()
        
        shopping_cart_page.wait_for_visible(shopping_cart_page.layer_container_locator)
        shopping_cart_page.wait_for_visible(shopping_cart_page.item_title_locator)
        shopping_cart_page.wait_for_visible(shopping_cart_page.item_price_locator)
        shopping_cart_page.wait_for_visible(shopping_cart_page.item_amount_locator)
    
    
    def test_verify_product_in_cart(self, driver):
        
        shopping_cart_page = ShoppingCartPage(driver)
        assert shopping_cart_page.get_product_amount() == 1, "Product not found in cart"
        assert shopping_cart_page.get_item_title() == "人氣回購TOP3⭐泰式打拋豬花椰菜米+墨西哥風味牛肉花椰菜米+三杯雞花椰菜米", "Incorrect product title"
        assert shopping_cart_page.get_item_price() == "NT$475", "Incorrect product price"
        assert shopping_cart_page.get_item_amount() == "1", "Incorrect product amount"