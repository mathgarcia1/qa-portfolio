import os
import threading
import time
import socket
import pytest
import uvicorn
from app.main import app

def wait_for_port(host, port, timeout=5.0):
    """Aguarda até que a porta especificada esteja aberta no host."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.create_connection((host, port), timeout=0.5):
                return True
        except (ConnectionRefusedError, socket.timeout, OSError):
            time.sleep(0.1)
    return False

@pytest.fixture(scope="session")
def uvicorn_server():
    # Permite mudar a porta via variável de ambiente ou usa 8001 como fallback
    port = int(os.getenv("TEST_PORT", 8001))
    host = "127.0.0.1"
    
    def run_server():
        try:
            uvicorn.run(app, host=host, port=port, log_level="error")
        except Exception as e:
            # Em caso de erro crítico, o wait_for_port falhará
            pass
            
    thread = threading.Thread(target=run_server, daemon=True)
    thread.start()
    
    if not wait_for_port(host, port):
        raise RuntimeError(f"Servidor Uvicorn não iniciou na porta {port} após timeout.")
    
    yield f"http://{host}:{port}"

@pytest.fixture(scope="session")
def admin_credentials():
    return {
        "username": os.getenv("TEST_ADMIN_USER", "admin"),
        "password": os.getenv("TEST_ADMIN_PASS", "password123")
    }
