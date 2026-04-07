import os
from faker import Faker
from playwright.sync_api import Page, expect
from .pages.login_page import LoginPage
from .pages.admin_upload_page import AdminUploadPage

fake = Faker('pt_BR')

def test_xml_import_flow_success(page: Page, uvicorn_server, admin_credentials):
    """Fluxo Crítico: Upload de XML e verificação de dados no dashboard."""
    login_page = LoginPage(page)
    login_page.navigate(f"{uvicorn_server}/login")
    login_page.login(admin_credentials["username"], admin_credentials["password"])
    
    upload_page = AdminUploadPage(page)
    upload_page.navigate(f"{uvicorn_server}/admin/upload")
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    xml_path = os.path.join(base_path, "assets", "projeto_teste.xml")
    upload_page.upload_xml(xml_path)
    
    project_name = f"Projeto {fake.company()}"
    mapping = {'area': '10001', 'subarea': '10002', 'disciplina': '10003'}
    upload_page.fill_mapping(project_name, mapping)
    
    expect(page.locator(upload_page.success_msg)).to_contain_text("sucesso")
    
    # Validação do estado no Dashboard
    page.goto(f"{uvicorn_server}/")
    page.select_option('select[name="project_id"]', label=project_name)
    expect(page.locator("#disp_total")).to_have_text("1")
