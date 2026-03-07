# windows + r, cmd
# cd c:\Users\Ian\meu_projeto_fastapi
# python -m venv venv
# venv\Scripts\activate
# uvicorn main:app --reload
#..\.venv\Scripts\activate
#usar o alembic para criar as tabelas, mudar o arquivo alembic.ini para apontar para o banco de dados correto, depois rodar os seguintes comandos:

from fastapi import FastAPI
app = FastAPI()

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)