# windows + r, cmd
# cd c:\Users\Ian\meu_projeto_fastapi
# python -m venv venv
# venv\Scripts\activate
# uvicorn main:app --reload

from fastapi import FastAPI
app = FastAPI()

from auth_routes import auth_router
from order_routes import order_router

