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
load_dotenv() #carregando as variáveis de ambiente do arquivo .env para o ambiente de execução do aplicativo, permitindo o acesso a essas variáveis através do código
    

SECRET_KEY= os.getenv("SECRET_KEY") #obtendo o valor da variável de ambiente SECRET_KEY, que é usada para criptografar as senhas dos usuários, garantindo que a chave secreta seja mantida segura e não exposta no código-fonte

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
 #criando um objeto CryptContext configurado para usar o algoritmo de hash bcrypt, que é uma escolha segura para armazenar senhas, 
 #e definindo a opção deprecated como "auto" para lidar automaticamente com senhas antigas que possam ter sido hashadas com algoritmos menos seguros
from auth_routes import auth_router
from order_routes import order_router




app.include_router(auth_router)
app.include_router(order_router)