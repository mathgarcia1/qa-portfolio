import time
from playwright.sync_api import Page, expect
from .pages.login_page import LoginPage
from .pages.admin_users_page import AdminUsersPage

def test_admin_create_user(page: Page, uvicorn_server, admin_credentials):
    # 1. Login
    login_page = LoginPage(page)
    login_page.navigate(f"{uvicorn_server}/login")
    login_page.login(admin_credentials["username"], admin_credentials["password"])
    
    # 2. Navegar e Criar
    admin_page = AdminUsersPage(page)
    admin_page.navigate(f"{uvicorn_server}/admin/usuarios")
    
    new_username = f"user_test_{int(time.time())}"
    admin_page.go_to_new_user()
    admin_page.create_user(new_username, "pass123", "+5511000000000")
    
    expect(page.locator(admin_page.table_rows).filter(has_text=new_username)).to_be_visible()
