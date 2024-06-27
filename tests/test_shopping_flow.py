from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from pages.product_page import ProductPage
from pages.shopping_cart_page import ShoppingCartPage
from utils.constants import *


class TestShoppingFlow:
        
    def test_open_website(self, driver):
        """
        Test to open the target website.
        """
        home_page = HomePage(driver)
        home_page.open()

        expected_title = WEB_TITLE
        assert expected_title in driver.title, f"Title mismatch: expected '{expected_title}', got '{driver.title}'"

    def test_search_box_present(self, driver):
        """
        Test to search for a product by entering a search query and submitting it.
        1. Enter the search term into the search box and click the search button.
        3. Verify that the product list page is loaded.
        4. Verify that the search results contain products.
        """
        home_page = HomePage(driver)  
        assert home_page.is_search_box_present(), "Search box not found"

    def test_search_for_product(self, driver):
        """
        Test to search for a product by entering a search query and submitting it.
        """
        home_page = HomePage(driver)
        product_list_page = home_page.enter_search_term(SEARCH_TERM).click_search_button()
        
        assert product_list_page.is_loaded(), "Product list page not loaded"
        assert product_list_page.has_products(), "No products found in search results"
        
    def test_first_product_information(self, driver):
        """
        Test to verify the information of the first product in the product list.
        1. Retrieve the title of the first product in the product list.
        2. Verify that the first product's title contains the search term.
        3. Verify that the first product is clickable.
        """
        product_list_page = ProductListPage(driver)
        first_product_name = product_list_page.get_first_product_title()
  
        assert product_list_page.contain_term(first_product_name, SEARCH_TERM), f"First product does not contain search term '{SEARCH_TERM}', but got '{first_product_name}'"
        assert product_list_page.wait_for_clickable(product_list_page.product_item_locator), "First product is not clickable"

    def test_open_product_page(self, driver):
        """
        1. Test to open the first product's detail page from the search results.
        2. Wait for the product detail page to load and verifies its presence.
        """
        product_list_page = ProductListPage(driver)
        expected_product_name = product_list_page.get_first_product_title()
        
        product_page = product_list_page.click_first_product()
        actual_product_name = product_page.get_product_title()
        
        assert product_page.is_loaded(), "Failed to open product detail page"
        assert expected_product_name == actual_product_name, "Product name mismatch"
        
    def test_product_is_available(self, driver):
        """
        This test checks the presence and usability of key elements on the product page:
        - Quantity button
        - Add to cart button
        - Buy now button
        """
        product_page = ProductPage(driver)

        assert product_page.is_quantity_button_present(), "Quantity button not found"
        assert product_page.is_add_to_cart_button_present() and product_page.is_add_to_cart_button_clickable(), "Add to cart button not usable"
        assert product_page.is_immediately_buy_button_present(), "Buy now button not usable"

    def test_add_product_to_cart(self, driver, shared_data):
        """
        Test to add the product to the shopping cart.
        1. Add the product to the shopping cart.
        2. Store product details (name, price, amount) in shared_data.
        3. Verify that the product was successfully added to the cart.
        """
        product_page = ProductPage(driver)
        product_page.add_to_cart()
        
        shared_data["item_name"] = product_page.get_product_title()
        shared_data["item_price"] = product_page.get_product_price()
        shared_data["item_amount"] = product_page.get_product_amount()
        
        assert product_page.wait_for_visible(product_page.add_to_cart_success_locator), "Failed to add product to cart"
        assert product_page.wait_for_invisible(product_page.add_to_cart_success_locator), "Failed to close modal"
        assert HomePage(driver).get_cart_badge_amount() == "1", "Failed to add product to cart"
        
    def test_open_shopping_cart_page(self, driver):
        """
        Test to open the shopping cart page.
        1. Click the cart icon to open the shopping cart page.
        2. Verify that the shopping cart page is loaded.
        """
        home_page = HomePage(driver)
        shopping_cart_page = home_page.click_cart_icon()
        
        assert shopping_cart_page.is_cart_loaded(), "Shopping cart page not loaded"
    
    def test_verify_product_in_cart(self, driver, shared_data):
        """
        Test to verify the product details in the shopping cart.
        1. Verify the product amount in the shopping cart.
        2. Verify the product title, price, and amount match the expected values stored in shared_data.
        """
        shopping_cart_page = ShoppingCartPage(driver)
        
        assert shopping_cart_page.get_product_amount() == 1, "Product not found in cart"
        assert shopping_cart_page.get_item_title() == shared_data["item_name"], "Incorrect product title"
        assert shopping_cart_page.get_item_price() == shared_data["item_price"], "Incorrect product price"
        assert shopping_cart_page.get_item_amount() == shared_data["item_amount"], "Incorrect product amount"