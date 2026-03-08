# windows + r, cmd
# cd c:\Users\Ian\meu_projeto_fastapi
# python -m venv venv
# venv\Scripts\activate
# uvicorn main:app --reload
#..\.venv\Scripts\activate
#usar o alembic para criar as tabelas, mudar o arquivo alembic.ini para apontar para o banco de dados correto, depois rodar os seguintes comandos:


from passlib.context import CryptContext #importando a classe CryptContext do módulo passlib.context para lidar com a criptografia de senhas
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer #importando a classe OAuth2PasswordBearer do módulo fastapi.security para lidar com a autenticação usando o padrão OAuth2 com senhas
load_dotenv() #carregando as variáveis de ambiente do arquivo .env para o ambiente de execução do aplicativo, permitindo o acesso a essas variáveis através do código
    


app = FastAPI()

 #criando um objeto CryptContext configurado para usar o algoritmo de hash bcrypt, que é uma escolha segura para armazenar senhas, 
 #e definindo a opção deprecated como "auto" para lidar automaticamente com senhas antigas que possam ter sido hashadas com algoritmos menos seguros
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login") #criando um objeto OAuth2PasswordBearer configurado para usar a rota "login" como o endpoint para obter tokens de autenticação, permitindo que as rotas protegidas dependam desse esquema de autenticação para verificar a validade dos tokens fornecidos pelos clientes
from auth_routes import auth_router
from order_routes import order_router




app.include_router(auth_router)
app.include_router(order_router)