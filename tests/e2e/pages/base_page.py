from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    def navigate(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state('networkidle')
    def click(self, selector: str):
        self.page.click(selector)
    def fill(self, selector: str, value: str):
        self.page.fill(selector, value)
    def get_text(self, selector: str) -> str:
        return self.page.inner_text(selector)
