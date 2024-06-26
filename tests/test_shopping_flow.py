from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.constants import *

def test_open_website(helper):
    """
    Test to open the target website.
    """
    helper.visit(BASE_URL)

def test_search_for_product(helper):
    """
    1. Test to search for a product by entering a search query and submitting it.
    2. Waits for the search results to be displayed and verifies their presence.
    """
    helper.send_keys(By.ID, "ns-search-input", "花椰菜米")
    helper.send_keys(By.ID, "ns-search-input", Keys.RETURN)
   
    # Wait for search results to display
    search_results = helper.wait_for_element(By.CLASS_NAME, "product-container", 10)
    assert search_results is not None, "搜尋結果顯示失敗"

def test_open_product_page(helper):
    """
    1. Test to open the first product's detail page from the search results.
    2. Waits for the product detail page to load and verifies its presence.
    """
    helper.click_element(By.CSS_SELECTOR, ".product-container:first-child a")
    product_detail = helper.wait_for_element(By.ID, "SalePageIndexController", 10)
    assert product_detail is not None, "進入商品詳細頁面失敗"

def test_add_product_to_cart(helper):
    """
    Test to add the product to the shopping cart.
    """
    helper.click_element(By.CLASS_NAME, "add-to-cart-btn")

def test_verify_product_in_cart(helper):
    """
    Test to verify that the product was successfully added to the cart.
    1. Clicks the cart icon, waits for the cart item to be displayed,
    2. Checks if the expected product is present in the cart.
    """
    # Verify the product was successfully added to the cart
    helper.click_element(By.CLASS_NAME, "nav-shopping-cart")
    cart_item = helper.wait_for_element(By.CSS_SELECTOR, "[class*='TitleLink']", 10)
    assert cart_item is not None, "商品加入購物車失敗"
    # Check if the expected product is in the cart
    product_name = cart_item.text
    assert "花椰菜米" in product_name, "購物車中未找到期望的商品"