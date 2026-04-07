from fastapi import FastAPI, Request, Form, Response, Cookie
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import Optional, List
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Mock DB
MOCK_USERS = [
    {"id": 1, "username": "admin", "telefone_whatsapp": "5511999999999", "bi_reports": []},
    {"id": 2, "username": "admin_qa", "telefone_whatsapp": "5511000000001", "bi_reports": []},
    {"id": 3, "username": "user_qa", "telefone_whatsapp": "5511000000002", "bi_reports": []}
]
MOCK_BI_REPORTS = []
MOCK_PROJECTS = []

@app.get("/", response_class=HTMLResponse)
def home(request: Request, access_token: Optional[str] = Cookie(None)):
    if not access_token: return RedirectResponse(url="/login")
    return templates.TemplateResponse(request, "dashboard.html", {"projects": MOCK_PROJECTS})

@app.get("/login", response_class=HTMLResponse)
def login_get(request: Request):
    return templates.TemplateResponse(request, "login.html")

@app.post("/login")
def login_post(username: str = Form(...), password: str = Form(...)):
    if username and (password == "password123" or password == "user123"):
        response = RedirectResponse(url="/", status_code=303)
        response.set_cookie(key="access_token", value="fake-jwt-token")
        return response
    return RedirectResponse(url="/login?error=1", status_code=303)

@app.get("/admin/usuarios", response_class=HTMLResponse)
def admin_users(request: Request):
    return templates.TemplateResponse(request, "admin_users.html", {"users": MOCK_USERS})

@app.get("/admin/usuarios/novo", response_class=HTMLResponse)
def admin_users_new(request: Request):
    return templates.TemplateResponse(request, "admin_users_form.html", {"user": None, "bi_reports": MOCK_BI_REPORTS})

@app.get("/admin/usuarios/{user_id}/editar", response_class=HTMLResponse)
def admin_users_edit(request: Request, user_id: int):
    user = next((u for u in MOCK_USERS if u["id"] == user_id), None)
    return templates.TemplateResponse(request, "admin_users_form.html", {"user": user, "bi_reports": MOCK_BI_REPORTS})

@app.post("/admin/usuarios")
def admin_users_post(
    username: str = Form(...), 
    telefone_whatsapp: str = Form(...),
    user_id: Optional[int] = Form(None),
    bi_reports: List[str] = Form([])
):
    if user_id:
        user = next((u for u in MOCK_USERS if u["id"] == user_id), None)
        if user:
            user["username"] = username
            user["telefone_whatsapp"] = telefone_whatsapp
            user["bi_reports"] = bi_reports
    else:
        new_id = max([u["id"] for u in MOCK_USERS]) + 1 if MOCK_USERS else 1
        MOCK_USERS.append({"id": new_id, "username": username, "telefone_whatsapp": telefone_whatsapp, "bi_reports": bi_reports})
    return RedirectResponse(url="/admin/usuarios", status_code=303)

@app.get("/admin/upload", response_class=HTMLResponse)
def admin_upload(request: Request):
    return templates.TemplateResponse(request, "admin_upload.html", {"step": 1})

@app.post("/admin/upload")
def admin_upload_post(request: Request, step: int = Form(1), project_name: Optional[str] = Form(None)):
    if step == 1:
        return templates.TemplateResponse(request, "admin_upload.html", {"step": 2})
    if step == 2:
        if project_name:
            MOCK_PROJECTS.append({"id": len(MOCK_PROJECTS)+1, "name": project_name})
        return templates.TemplateResponse(request, "admin_upload.html", {"step": 3})
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
