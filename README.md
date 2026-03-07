# 🚀 Python FastAPI — REST API with Authentication

A REST API built with **FastAPI** and **Python**, featuring JWT authentication, user management, and order handling with SQLite.

---

## 📋 About

This project implements a structured REST API with:
- User registration and login with **JWT token authentication**
- Password hashing with **bcrypt**
- Order creation with user validation
- Database management with **SQLAlchemy** and **Alembic migrations**
- Environment variable management with **dotenv**

---

## 🛠️ Tech Stack

| Technology | Description |
|---|---|
| Python 3.14+ | Main language |
| FastAPI | Modern async web framework |
| Uvicorn | ASGI server |
| SQLAlchemy | ORM for database management |
| Alembic | Database migrations |
| Passlib + bcrypt | Password hashing |
| Python-Jose | JWT token generation |
| Pydantic | Data validation and schemas |
| Python-dotenv | Environment variable management |

---

## ⚡ Getting Started

### Prerequisites
- Python 3.10+
- pip or uv

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/IanRMarques/Python-FastAPI.git
cd Python-FastAPI

# 2. Create and activate virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate

# 3. Install dependencies
python -m pip install fastapi uvicorn sqlalchemy alembic passlib[bcrypt] python-jose[cryptography] python-dotenv sqlalchemy_utils bcrypt==4.0.1
```

### Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> ⚠️ **Never commit your `.env` file!** It is already listed in `.gitignore`.

---

## 🗄️ Database Setup

```bash
# 1. Initialize Alembic (first time only)
alembic init alembic

# 2. In alembic.ini, set the database URL:
#    sqlalchemy.url = sqlite:///.database.db

# 3. In alembic/env.py, add:
#    from models import Base
#    target_metadata = Base.metadata

# 4. Generate migration
alembic revision --autogenerate -m "initial migrate"

# 5. Apply migration
alembic upgrade head
```

> After the first setup, only repeat steps 4 and 5 whenever you change `models.py`.

---

## ▶️ Running the Server

```bash
uvicorn main:app --reload
```

The API will be available at: **http://127.0.0.1:8000**

---

## 📁 Project Structure

```
📦 Python-FastAPI/
├── main.py            # App entry point and FastAPI instance
├── auth_routes.py     # Authentication routes (register, login)
├── order_routes.py    # Order routes
├── models.py          # SQLAlchemy database models
├── schemas.py         # Pydantic validation schemas
├── dependencies.py    # Shared dependencies (session, bcrypt, config)
├── alembic/           # Database migrations
├── alembic.ini        # Alembic configuration
├── .env               # Environment variables (do not commit!)
├── .gitignore         # Git ignored files
└── README.md          # This file
```

---

## 🔗 API Endpoints

### Auth — `/auth`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/auth/` | Auth route health check |
| POST | `/auth/create_user` | Register a new user |
| POST | `/auth/login` | Login and receive a JWT token |

### Orders — `/pedidos`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/pedidos/` | Orders route health check |
| POST | `/pedidos/pedido` | Create a new order |

---

## 📖 Interactive Documentation

FastAPI generates automatic docs. With the server running, visit:

- **Swagger UI** → http://127.0.0.1:8000/docs
- **ReDoc** → http://127.0.0.1:8000/redoc

---

## 🔐 Authentication Flow

1. Register a user via `POST /auth/create_user`
2. Login via `POST /auth/login` — you will receive a **JWT access token**
3. Use the token in the `Authorization: Bearer <token>` header for protected routes

---

## 📝 Notes

- Passwords are hashed with **bcrypt** before being stored — plain text passwords are never saved
- JWT tokens expire after the time defined in `ACCESS_TOKEN_EXPIRE_MINUTES`
- The database file `.database.db` is local only and not versioned
