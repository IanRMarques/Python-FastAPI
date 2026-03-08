# 🚀 Python FastAPI — REST API with JWT Auth

A modern REST API built with **FastAPI** and **Python**, featuring JWT authentication, password hashing, and full database integration via SQLAlchemy.

> 🚧 **Status: Em desenvolvimento** — novas rotas e funcionalidades sendo adicionadas.

---

## 📋 About

This project demonstrates how to build a structured REST API with FastAPI, including:
- User registration and login with **JWT token authentication**
- **Password hashing** with bcrypt via Passlib
- **Database ORM** with SQLAlchemy + SQLite
- **Database migrations** with Alembic
- Organized route structure with APIRouter

---

## 🛠️ Tech Stack

| Technology | Version | Description |
|---|---|---|
| Python | 3.10+ | Main language |
| FastAPI | 0.135+ | Modern async web framework |
| Uvicorn | 0.41+ | ASGI server |
| SQLAlchemy | 2.0+ | Database ORM |
| Alembic | 1.x | Database migrations |
| Passlib + bcrypt | 1.7+ | Password hashing |
| Python-Jose | 3.5+ | JWT tokens |
| Python-dotenv | — | Environment variables |

---

## ⚡ Getting Started

### Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)

### Step by step

```bash
# 1. Clone the repository
git clone https://github.com/IanRMarques/Python-FastAPI.git
cd Python-FastAPI

# 2. Create and activate the virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows
source .venv/bin/activate     # Linux/Mac

# 3. Install dependencies
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] python-dotenv python-multipart sqlalchemy_utils alembic

# 4. Set up the database
alembic upgrade head

# 5. Run the server
uvicorn main:app --reload
```

✅ API running at: **http://127.0.0.1:8000**

---

## 📁 Project Structure

```
📦 Python-FastAPI/
├── main.py            # App entry point, router registration
├── auth_routes.py     # Authentication routes (register, login)
├── order_routes.py    # Order routes (CRUD)
├── models.py          # SQLAlchemy models (Usuario, Pedido, ItemPedido)
├── schemas.py         # Pydantic schemas for request/response validation
├── dependencies.py    # Shared dependencies (DB session, JWT config, bcrypt)
├── alembic/           # Database migration files
├── alembic.ini        # Alembic configuration
├── .env               # Environment variables (do not version!)
├── .gitignore
└── README.md
```

---

## 🔗 Endpoints

| Method | Route | Description | Auth |
|---|---|---|---|
| POST | `/auth/register` | Register a new user | ❌ |
| POST | `/auth/login` | Login and receive JWT token | ❌ |
| GET | `/pedidos` | List orders | ✅ |
| POST | `/pedidos` | Create a new order | ✅ |

> 🔒 Routes marked with ✅ require a valid JWT token in the `Authorization: Bearer <token>` header.

---

## 📖 Interactive Documentation

FastAPI generates automatic documentation. With the server running, visit:

- **Swagger UI** → http://127.0.0.1:8000/docs
- **ReDoc** → http://127.0.0.1:8000/redoc

---

## 📝 Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> ⚠️ **Never commit your `.env` file!** It's already in `.gitignore`.

---

## 🌱 How JWT Auth works in this project

```
1. User registers → password is hashed with bcrypt → stored in DB
2. User logs in → password is verified → JWT token is generated
3. Protected routes → token is validated → user ID is extracted
```
