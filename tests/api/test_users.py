import pytest
from fastapi.testclient import TestClient
from app.main import app, MOCK_USERS

client = TestClient(app)

def test_api_list_users():
    """GET /admin/usuarios: Deve listar todos os usuários mockados."""
    response = client.get("/admin/usuarios")
    assert response.status_code == 200
    assert any(u["username"] == "admin" for u in MOCK_USERS)

def test_api_create_user():
    """POST /admin/usuarios: Persistência de novo usuário via formulário."""
    new_user_data = {
        "username": "api_test_user",
        "telefone_whatsapp": "5518999999999",
        "bi_reports": []
    }
    response = client.post("/admin/usuarios", data=new_user_data, follow_redirects=False)
    assert response.status_code == 303
    assert any(u["username"] == "api_test_user" for u in MOCK_USERS)

@pytest.mark.xfail(reason="Vulnerabilidade IDOR: Acesso administrativo sem token.")
def test_api_unauthorized_access_to_users_list():
    """Valida se endpoints administrativos estão protegidos (Shift-Left Security)."""
    with TestClient(app) as guest_client:
        response = guest_client.get("/admin/usuarios")
    assert response.status_code != 200
