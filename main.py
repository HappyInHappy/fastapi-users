from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from api.auth import router as auth_router
from api.users import router as users_router
import os

app = FastAPI()
app.include_router(auth_router)
app.include_router(users_router)

static_dir = os.path.join(os.path.dirname(__file__), "templates")
if os.path.exists(static_dir):
    app.mount("/templates", StaticFiles(directory="templates"), name="templates")

@app.get("/login", response_class=HTMLResponse)
def login_page():
    with open("templates/login.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/register", response_class=HTMLResponse)
def register_page():
    with open("templates/register.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/admin", response_class=HTMLResponse)
def admin_page():
    with open("templates/admin.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
