from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = 'input[name="username"]'
        self.password_input = 'input[name="password"]'
        self.submit_button = 'button[type="submit"]'
        self.error_alert = '.alert-danger'

    def login(self, username, password):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.submit_button)
        self.page.wait_for_load_state('networkidle')
