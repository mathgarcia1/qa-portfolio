from playwright.sync_api import Page, expect
from .pages.login_page import LoginPage

def test_login_success(page: Page, uvicorn_server, admin_credentials):
    # 1. Login
    login_page = LoginPage(page)
    login_page.navigate(f"{uvicorn_server}/login")
    login_page.login(admin_credentials["username"], admin_credentials["password"])
    
    expect(page).to_have_url(f"{uvicorn_server}/")
    
    cookies = page.context.cookies()
    token_cookie = next((c for c in cookies if c["name"] == "access_token"), None)
    assert token_cookie is not None

def test_login_failure(page: Page, uvicorn_server):
    login_page = LoginPage(page)
    login_page.navigate(f"{uvicorn_server}/login")
    login_page.login("invalid_user", "wrong_password")
    
    expect(page.locator(".alert-danger")).to_be_visible()
