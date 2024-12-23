from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    def select_first_product(self):
        self.page.click("div.product-item:first-child a")
