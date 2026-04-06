from .base_page import BasePage

class AdminUsersPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.new_user_btn = 'a[href="/admin/usuarios/novo"]'
        self.username_input = 'input[name="username"]'
        self.password_input = 'input[name="password"]'
        self.phone_input = 'input[name="telefone_whatsapp"]'
        self.save_btn = 'button:has-text("Salvar")'
        self.table_rows = '.table tbody tr'

    def create_user(self, username, password, phone):
        self.click(self.new_user_btn)
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.fill(self.phone_input, phone)
        self.click(self.save_btn)
