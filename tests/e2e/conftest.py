import os, threading, time, pytest, uvicorn
from app.main import app

@pytest.fixture(scope="session")
def uvicorn_server():
    port = 8001
    def run_server():
        uvicorn.run(app, host="127.0.0.1", port=port, log_level="error")
    thread = threading.Thread(target=run_server, daemon=True)
    thread.start()
    time.sleep(1)
    yield f"http://127.0.0.1:{port}"

@pytest.fixture(scope="session")
def admin_credentials():
    return {"username": "admin_qa", "password": "password123"}

@pytest.fixture(scope="session")
def user_credentials():
    return {"username": "user_qa", "password": "user123"}
