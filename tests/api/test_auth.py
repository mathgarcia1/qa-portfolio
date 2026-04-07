from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_api_login_success():
    """POST /login: Deve gerar set-cookie com access_token válido."""
    payload = {"username": "admin", "password": "password123"}
    response = client.post("/login", data=payload, follow_redirects=False)
    
    assert response.status_code == 303
    assert response.headers["location"] == "/"
    assert "access_token" in response.cookies
    assert response.cookies["access_token"] == "fake-jwt-token"

def test_api_login_failure():
    """POST /login: Credenciais inválidas devem redirecionar para tela de erro."""
    payload = {"username": "admin", "password": "wrongpassword"}
    response = client.post("/login", data=payload, follow_redirects=False)
    
    assert response.status_code == 303
    assert response.headers["location"] == "/login?error=1"
    assert "access_token" not in response.cookies
