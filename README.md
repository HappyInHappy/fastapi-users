# FastAPI 用户管理系统

一个基于 FastAPI 框架开发的用户管理系统，包含用户登录、注册、权限管理、用户状态控制等功能。

## 功能特性

- ✅ 用户登录与认证
- ✅ 用户注册功能
- ✅ 基于 token 的身份验证
- ✅ 记住密码功能
- ✅ 用户状态管理（活跃/停用）
- ✅ 角色权限控制（管理员/普通用户）
- ✅ 用户管理后台
- ✅ 登录失败提示
- ✅ 完整的用户 CRUD 操作
- ✅ 用户列表分页功能
- ✅ 用户搜索功能
- ✅ 数据统计（用户总数、活跃用户数、访问量）
- ✅ 响应式设计

## 技术栈

- **后端**: FastAPI + Python 3.10+
- **前端**: HTML + CSS + JavaScript
- **数据存储**: JSON 文件
- **服务器**: Uvicorn

## 项目结构

```
fastapi-users/
├── api/                 # API 路由模块
│   ├── auth.py          # 认证相关接口（登录、注册、验证）
│   └── users.py         # 用户管理接口（CRUD 操作）
├── templates/           # 前端模板
│   ├── login.html       # 登录页面
│   ├── register.html    # 注册页面
│   └── admin.html       # 后台管理页面
├── main.py              # 主应用入口
├── users.json           # 用户数据存储
├── requirements.txt     # 项目依赖
└── venv/                # 虚拟环境
```

## 快速开始

### 1. 安装依赖

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows
venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 启动服务器

```bash
uvicorn main:app --reload
```

服务器将运行在 `http://127.0.0.1:8000`

## 访问地址

- **登录页面**: `http://127.0.0.1:8000/login`
- **注册页面**: `http://127.0.0.1:8000/register`
- **后台管理**: `http://127.0.0.1:8000/admin`
- **API 文档**: `http://127.0.0.1:8000/docs`

## 测试账号

| 用户名 | 密码 | 角色 | 状态 |
|--------|------|------|------|
| admin | 123456 | 管理员 | 活跃 |
| user01 | password123 | 用户 | 活跃 |
| user02 | password456 | 用户 | 停用 |

## API 接口

### 认证接口
- `POST /auth/login` - 用户登录
- `POST /auth/register` - 用户注册
- `POST /auth/verify` - 验证 token

### 用户管理接口
- `GET /users/` - 获取所有用户
- `PUT /users/{id}` - 更新用户信息
- `DELETE /users/{id}` - 删除用户
- `GET /users/count` - 获取用户总数
- `GET /users/count/active` - 获取活跃用户数

## 功能说明

### 登录功能
- 支持用户名密码登录
- 支持记住密码
- 登录失败时显示错误提示
- 停用账号无法登录

### 注册功能
- 支持用户名、邮箱、电话、密码注册
- 表单验证
- 注册成功后自动跳转到登录页面
- 注册成功提示

### 后台管理
- 查看所有用户列表
- 支持分页（每页 5 条记录）
- 支持搜索用户名和邮箱
- 编辑用户信息（邮箱、电话、角色、状态）
- 删除用户
- 查看用户详情
- 数据统计（用户总数、活跃用户数、访问量）

## 注意事项

- 本项目使用 JSON 文件存储用户数据，仅用于演示目的
- 生产环境建议使用数据库存储
- 密码未加密存储，生产环境需使用哈希加密
- token 存储在前端 localStorage 中
- 用户 ID 由系统自动生成，保持连续顺序

## 许可证

MIT License