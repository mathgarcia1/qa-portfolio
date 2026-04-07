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

    def navigate_to_list(self, base_url=""):
        self.navigate(f"{base_url}/admin/usuarios")

    def go_to_new_user(self):
        self.click(self.new_user_btn)

    def create_user(self, username, password, phone):
        # Note: If called after go_to_new_user, the button might not be visible.
        # But we keep it for backward compatibility if needed.
        if self.page.locator(self.new_user_btn).is_visible():
            self.click(self.new_user_btn)
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.fill(self.phone_input, phone)
        self.click(self.save_btn)

    def edit_user(self, username):
        self.page.get_by_role("row", name=username).get_by_role("link", name="Editar").click()

    def toggle_bi_report(self, title):
        self.page.get_by_label(title).check()

    def save_user(self):
        self.click(self.save_btn)
