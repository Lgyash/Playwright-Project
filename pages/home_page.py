from pages.base_page import BasePage

class HomePage(BasePage):
    def search(self, query: str):
        self.page.fill("input[name='q']", query)
        self.page.click("button[type='submit']")
