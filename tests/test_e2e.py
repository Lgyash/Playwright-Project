import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage

@pytest.fixture
def setup(page):
    # Base URL for the e-commerce site
    base_url = "https://example-ecommerce.com"
    home = HomePage(page)
    home.navigate(base_url)
    return page, home

def test_add_to_cart(setup):
    page, home = setup
    search_results = SearchResultsPage(page)
    cart = CartPage(page)

    # Search for a product
    home.search("laptop")
    
    # Select the first product
    search_results.select_first_product()
    
    # Add to cart
    page.click("button.add-to-cart")
    
    # Go to cart
    page.click("a[href='/cart']")
    
    # Validate cart
    cart.validate_cart_item("laptop")
