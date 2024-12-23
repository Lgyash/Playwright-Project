from pages.base_page import BasePage

class CartPage(BasePage):
    def validate_cart_item(self, product_name: str):
        assert product_name in self.page.text_content("div.cart-items")
