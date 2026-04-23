from fastapi import APIRouter
import json
import os

router = APIRouter(prefix="/users", tags=["用户管理"])

def load_users():
    config_path = os.path.join(os.path.dirname(__file__), "..", "users.json")
    with open(config_path, "r", encoding="utf-8") as f:
        users = json.load(f)
    # 为用户添加ID
    for i, user in enumerate(users, 1):
        user["id"] = i
    return users

@router.get("/")
def get_users():
    users = load_users()
    return {"users": users}

@router.put("/{user_id}")
def update_user(user_id: int, data: dict):
    users = load_users()
    for user in users:
        if user["id"] == user_id:
            user["email"] = data.get("email", user["email"])
            user["phone"] = data.get("phone", user.get("phone", ""))
            user["role"] = data.get("role", user["role"])
            user["status"] = data.get("status", user["status"])
            config_path = os.path.join(os.path.dirname(__file__), "..", "users.json")
            # 保存时移除ID
            users_to_save = [{k: v for k, v in u.items() if k != "id"} for u in users]
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump(users_to_save, f, ensure_ascii=False, indent=4)
            return {"message": "更新成功"}
    return {"error": "用户不存在"}

@router.delete("/{user_id}")
def delete_user(user_id: int):
    users = load_users()
    users = [u for u in users if u["id"] != user_id]
    config_path = os.path.join(os.path.dirname(__file__), "..", "users.json")
    # 保存时移除ID
    users_to_save = [{k: v for k, v in user.items() if k != "id"} for user in users]
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(users_to_save, f, ensure_ascii=False, indent=4)
    return {"message": "删除成功"}

@router.get("/count")
def get_user_count():
    users = load_users()
    return {"count": len(users)}

@router.get("/count/active")
def get_active_user_count():
    users = load_users()
    active_users = [user for user in users if user.get("status") == "active"]
    return {"count": len(active_users)}
