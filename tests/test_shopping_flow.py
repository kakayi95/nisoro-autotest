import pytest
from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from pages.product_page import ProductPage
from pages.shopping_cart_page import ShoppingCartPage


class TestShoppingFlow:
        
    def test_open_website(self, driver):
        """
        Test to open the target website.
        """
        home_page = HomePage(driver)
        home_page.open()


    def test_search_for_product(self, driver):
        """
        1. Test to search for a product by entering a search query and submitting it.
        2. Waits for the search results to be displayed and verifies their presence.
        """
        home_page = HomePage(driver)
        search_results = home_page.search_product("花椰菜米")
        assert search_results is not None, "搜尋結果顯示失敗"

    def test_open_product_page(self, driver):
        """
        1. Test to open the first product's detail page from the search results.
        2. Waits for the product detail page to load and verifies its presence.
        """
        product_list_page = ProductListPage(driver)
        product_detail = product_list_page.click_first_product()
        assert product_detail is not None, "進入商品詳細頁面失敗"

    def test_add_product_to_cart(self, driver):
        """
        Test to add the product to the shopping cart.
        """
        product_page = ProductPage(driver)
        product_page.add_to_cart()

    def test_verify_product_in_cart(self, driver):
        """
        Test to verify that the product was successfully added to the cart.
        1. Clicks the cart icon, waits for the cart item to be displayed,
        2. Checks if the expected product is present in the cart.
        """
        # Verify the product was successfully added to the cart
        home_page = HomePage(driver)
        cart_item = home_page.click_cart_icon()
        assert cart_item is not None, "商品加入購物車失敗"
        # Check if the expected product is in the cart
        shopping_cart_page = ShoppingCartPage(driver)
        product_name = shopping_cart_page.get_cart_item_text()
        assert "花椰菜米" in product_name, "購物車中未找到期望的商品"