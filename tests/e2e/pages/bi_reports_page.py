import re
from playwright.sync_api import expect
from .base_page import BasePage

class AdminBiReportsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.new_report_btn = 'a[href="/admin/bi-reports/novo"]'
        self.title_input = 'input[name="title"]'
        self.embed_url_input = 'textarea[name="embed_url"]'
        self.save_btn = 'button:has-text("Salvar")'
        self.table_rows = '.table tbody tr'

    def create_report(self, title, embed_url):
        # We handle both clicking the button if on the list page
        # or just filling if on the form page.
        if self.page.locator(self.new_report_btn).is_visible():
            self.click(self.new_report_btn)
        self.fill(self.title_input, title)
        self.fill(self.embed_url_input, embed_url)
        self.click(self.save_btn)

class UserBiPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.sidebar_reports = '.list-group-item'

    def navigate_to_bi(self, uvicorn_server=None):
        if uvicorn_server:
            self.page.goto(f"{uvicorn_server}/powerbi")
        else:
            self.page.goto("/powerbi")

    def is_report_visible(self, title):
        return self.page.get_by_text(title).is_visible()
