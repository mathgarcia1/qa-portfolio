from fastapi import FastAPI, Request, Form, Response, Cookie
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import Optional
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Mock DB
MOCK_USERS = [{"username": "admin", "telefone_whatsapp": "5511999999999"}]
MOCK_BI_REPORTS = []

@app.get("/", response_class=HTMLResponse)
def home(request: Request, access_token: Optional[str] = Cookie(None)):
    if not access_token: return RedirectResponse(url="/login")
    return templates.TemplateResponse(request, "dashboard.html")

@app.get("/login", response_class=HTMLResponse)
def login_get(request: Request):
    return templates.TemplateResponse(request, "login.html")

@app.post("/login")
def login_post(username: str = Form(...), password: str = Form(...)):
    if username and password == "password123":
        response = RedirectResponse(url="/", status_code=303)
        response.set_cookie(key="access_token", value="fake-jwt-token")
        return response
    return RedirectResponse(url="/login?error=1", status_code=303)

@app.get("/admin/usuarios", response_class=HTMLResponse)
def admin_users(request: Request):
    return templates.TemplateResponse(request, "admin_users.html", {"users": MOCK_USERS})

@app.get("/admin/usuarios/novo", response_class=HTMLResponse)
def admin_users_new(request: Request):
    return templates.TemplateResponse(request, "admin_users_form.html")

@app.post("/admin/usuarios")
def admin_users_post(username: str = Form(...), telefone_whatsapp: str = Form(...)):
    MOCK_USERS.append({"username": username, "telefone_whatsapp": telefone_whatsapp})
    return RedirectResponse(url="/admin/usuarios", status_code=303)

@app.get("/admin/upload", response_class=HTMLResponse)
def admin_upload(request: Request):
    return templates.TemplateResponse(request, "admin_upload.html", {"step": 1})

@app.post("/admin/upload")
def admin_upload_post(request: Request, step: int = Form(1)):
    if step == 1:
        return templates.TemplateResponse(request, "admin_upload.html", {"step": 2})
    return templates.TemplateResponse(request, "admin_upload.html", {"step": 3})

@app.get("/admin/bi-reports", response_class=HTMLResponse)
def admin_bi(request: Request):
    return templates.TemplateResponse(request, "admin_bi.html", {"reports": MOCK_BI_REPORTS})

@app.get("/admin/bi-reports/novo", response_class=HTMLResponse)
def admin_bi_new(request: Request):
    return templates.TemplateResponse(request, "admin_bi_form.html")

@app.post("/admin/bi-reports")
def admin_bi_post(title: str = Form(...)):
    MOCK_BI_REPORTS.append({"title": title})
    return RedirectResponse(url="/admin/bi-reports", status_code=303)

@app.get("/powerbi", response_class=HTMLResponse)
def powerbi(request: Request):
    return templates.TemplateResponse(request, "powerbi.html", {"reports": MOCK_BI_REPORTS})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
