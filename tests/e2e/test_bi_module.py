import time
from playwright.sync_api import Page, expect
from .pages.login_page import LoginPage
from .pages.bi_reports_page import AdminBiReportsPage, UserBiPage
from .pages.admin_users_page import AdminUsersPage

def test_bi_flow(page: Page, uvicorn_server, admin_credentials, user_credentials):
    # 1. Login Admin e Criar Relatório
    login_page = LoginPage(page)
    login_page.navigate(f"{uvicorn_server}/login")
    login_page.login(admin_credentials["username"], admin_credentials["password"])
    
    admin_bi_page = AdminBiReportsPage(page)
    admin_bi_page.navigate(f"{uvicorn_server}/admin/bi-reports")
    
    report_title = f"Report_{int(time.time())}"
    embed_url = "https://app.powerbi.com/reportEmbed?reportId=dummy"
    admin_bi_page.create_report(report_title, embed_url)
    
    # 2. Conceder Permissão
    admin_users_page = AdminUsersPage(page)
    admin_users_page.navigate_to_list(uvicorn_server)
    admin_users_page.edit_user(user_credentials["username"])
    admin_users_page.toggle_bi_report(report_title)
    admin_users_page.save_user()
    
    # 3. Validar Acesso do Usuário
    page.context.clear_cookies()
    login_page.navigate(f"{uvicorn_server}/login")
    login_page.login(user_credentials["username"], user_credentials["password"])
    
    user_bi_page = UserBiPage(page)
    user_bi_page.navigate_to_bi(uvicorn_server)
    expect(page.get_by_role('link', name=report_title)).to_be_visible()
