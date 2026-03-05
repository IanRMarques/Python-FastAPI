# 🚀 My First FastAPI + Python Project

A modern, fast and easy-to-use REST API — built with **FastAPI** and **Python**.

---

## 📋 About

This project is a basic example of how to build a REST API with FastAPI, including authentication and route organization. Perfect for those getting started with API development in Python.

---

## 🛠️ Tech Stack

| Technology | Version | Description |
|---|---|---|
| Python | 3.14+ | Main language |
| FastAPI | 0.135+ | Modern web framework |
| Uvicorn | 0.41+ | ASGI server |
| SQLAlchemy | 2.0+ | Database ORM |
| Passlib | 1.7+ | Password hashing |
| Python-Jose | 3.5+ | JWT tokens |

---

## ⚡ Getting Started

### Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv) (package manager)

### Step by step

```bash
# 1. Clone the repository
git clone https://github.com/your-username/your-repository.git
cd your-repository

# 2. Create and activate the virtual environment
uv venv
.venv\Scripts\Activate.ps1   # Windows
source .venv/bin/activate     # Linux/Mac

# 3. Install dependencies
uv pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] python-dotenv python-multipart

# 4. Run the server
uvicorn main:app --reload
```

✅ The API will be available at: **http://127.0.0.1:8000**

---

## 📁 Project Structure

```
📦 my-project/
├── main.py            # Main application file
├── auth_routes.py     # Authentication routes
├── order_routes.py    # Order routes
├── .env               # Environment variables (do not version!)
├── .gitignore         # Git ignored files
└── README.md          # This file
```

---

## 🔗 Endpoints

### Authentication
| Method | Route | Description |
|---|---|---|
| POST | `/auth/login` | User login |
| POST | `/auth/register` | User registration |

### Orders
| Method | Route | Description |
|---|---|---|
| GET | `/pedidos/` | List all orders |
| POST | `/pedidos/` | Create a new order |

---

## 📖 Interactive Documentation

FastAPI generates automatic documentation! With the server running, visit:

- **Swagger UI** → http://127.0.0.1:8000/docs
- **ReDoc** → http://127.0.0.1:8000/redoc

---

## 🌱 First Steps with FastAPI

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, world! 🚀"}
```

It's that simple! This single file already creates a fully working API.

---

## 📝 Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///./database.db
```

> ⚠️ **Never version your `.env` file!** It's already in `.gitignore`.
