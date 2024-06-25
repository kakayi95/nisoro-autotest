from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_open_website(driver):
    """
    Test to open the target website.
    """
    driver.get("https://www.nisoro.com/")

def test_search_for_product(driver):
    """
    1. Test to search for a product by entering a search query and submitting it.
    2. Waits for the search results to be displayed and verifies their presence.
    """
    search_box = driver.find_element(By.ID, "ns-search-input")
    search_box.send_keys("花椰菜米")
    search_box.send_keys(Keys.RETURN)
    # Wait for search results to display
    search_results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-container"))
    )
    assert search_results is not None, "搜尋結果顯示失敗"

def test_open_product_page(driver):
    """
    1. Test to open the first product's detail page from the search results.
    2. Waits for the product detail page to load and verifies its presence.
    """
    first_product = driver.find_element(By.CSS_SELECTOR, ".product-container:first-child a")
    first_product.click()
    product_detail = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "SalePageIndexController"))
    )
    assert product_detail is not None, "進入商品詳細頁面失敗"

def test_add_product_to_cart(driver):
    """
    Test to add the product to the shopping cart.
    """
    add_to_cart_button = driver.find_element(By.CLASS_NAME, "add-to-cart-btn")
    add_to_cart_button.click()

def test_verify_product_in_cart(driver):
    """
    Test to verify that the product was successfully added to the cart.
    1. Clicks the cart icon, waits for the cart item to be displayed,
    2. Checks if the expected product is present in the cart.
    """
    # Verify the product was successfully added to the cart
    cart_icon = driver.find_element(By.CLASS_NAME, "nav-shopping-cart")
    cart_icon.click()
    cart_item = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='TitleLink']"))
    )
    assert cart_item is not None, "商品加入購物車失敗"
    # Check if the expected product is in the cart
    product_name = cart_item.text
    assert "花椰菜米" in product_name, "購物車中未找到期望的商品"
