from fastapi import APIRouter, Response, HTTPException
from pydantic import BaseModel
import json
import os
import uuid

router = APIRouter(prefix="/auth", tags=["认证"])

tokens = {}

class LoginRequest(BaseModel):
    username: str
    password: str

def load_users():
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "users.json")
    with open(config_path, "r", encoding="utf-8") as f:
        users = json.load(f)
    # 为用户添加ID
    for i, user in enumerate(users, 1):
        user["id"] = i
    return users

@router.post("/login")
def login(request: LoginRequest, response: Response):
    if not request.username or not request.username.strip():
        response.status_code = 400
        return {"error": "用户名不能为空"}
    if not request.password or not request.password.strip():
        response.status_code = 400
        return {"error": "密码不能为空"}
    users = load_users()
    for user in users:
        if user["username"] == request.username and user["password"] == request.password:
            if user.get("status") == "inactive":
                response.status_code = 403
                return {"error": "账号已被停用，请联系管理员"}
            token = str(uuid.uuid4())
            tokens[token] = {"username": user["username"], "user_id": user["id"], "role": user["role"]}
            return {"access_token": token, "token_type": "bearer"}
    response.status_code = 401
    return {"error": "用户名或密码错误"}

@router.post("/register")
def register(user_data: dict, response: Response):
    username = user_data.get("username")
    email = user_data.get("email")
    password = user_data.get("password")
    phone = user_data.get("phone")

    if not username or not username.strip():
        response.status_code = 400
        return {"error": "用户名不能为空"}
    if not email or not email.strip():
        response.status_code = 400
        return {"error": "邮箱不能为空"}
    if not password or len(password) < 6:
        response.status_code = 400
        return {"error": "密码长度至少6位"}
    if not phone or not phone.strip():
        response.status_code = 400
        return {"error": "电话不能为空"}
    
    users = load_users()
    for user in users:
        if user["username"] == username:
            response.status_code = 400
            return {"error": "用户名已存在"}
        if user["email"] == email:
            response.status_code = 400
            return {"error": "邮箱已被注册"}
    
    new_user = {
        "username": username,
        "password": password,
        "email": email,
        "phone": phone,
        "role": "user",
        "status": "active"
    }
    users.append(new_user)
    
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "users.json")
    # 保存时移除ID
    users_to_save = [{k: v for k, v in user.items() if k != "id"} for user in users]
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(users_to_save, f, ensure_ascii=False, indent=4)
    
    return {"message": "注册成功"}

@router.post("/verify")
def verify_token(request: dict):
    token = request.get("token")
    if not token or token not in tokens:
        raise HTTPException(status_code=401, detail="未登录或token已过期")
    return {"valid": True, "username": tokens[token]["username"], "role": tokens[token]["role"]}
