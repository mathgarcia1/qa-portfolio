from playwright.sync_api import Page, expect
from .pages.login_page import LoginPage
from .pages.admin_users_page import AdminUsersPage

def test_full_admin_flow(page: Page, uvicorn_server, admin_credentials):
    # 1. Login
    login_page = LoginPage(page)
    login_page.navigate(f"{uvicorn_server}/login")
    login_page.login(admin_credentials["username"], admin_credentials["password"])
    
    # 2. Redirect check
    expect(page).to_have_url(f"{uvicorn_server}/")
    
    # 3. Create User
    admin_users = AdminUsersPage(page)
    admin_users.navigate(f"{uvicorn_server}/admin/usuarios")
    admin_users.create_user("qa_tester", "secure_pass", "5511000000000")
    
    # 4. Verify in List
    expect(page.locator(admin_users.table_rows).filter(has_text="qa_tester")).to_be_visible()
