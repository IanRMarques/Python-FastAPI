from models import db
from sqlalchemy.orm import sessionmaker #importando a classe sessionmaker do SQLAlchemy para criar sessões de banco de dados
from passlib.context import CryptContext
import os
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def pegar_sessao():
    try:
        session = sessionmaker(bind=db) #criando uma classe de sessão vinculada ao engine do banco de dados
        session = session() #criando uma instância de sessão para interagir com o banco de dados
        yield session #utilizando yield para criar um gerador que retorna a sessão, permitindo que o FastAPI gerencie o ciclo de vida da sessão de forma eficiente
        session.close() #fechando a sessão após o uso 
    finally: #garantindo que aconteça caso de erro, sem tratamento de erros
         session.close()

SECRET_KEY= os.getenv("SECRET_KEY") #obtendo o valor da variável de ambiente SECRET_KEY, que é usada para criptografar as senhas dos usuários, 
#garantindo que a chave secreta seja mantida segura e não exposta no código-fonte

ALGORITHM = os.getenv("ALGORITHM") #obtendo o valor da variável de ambiente ALGORITHM, que define o algoritmo de criptografia a ser usado para gerar tokens de autenticação

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")) #obtendo o valor da variável de ambiente ACCESS_TOKEN_EXPIRE_MINUTES, 
#que define o tempo de expiração para os tokens de acesso gerados, convertendo-o para um inteiro para uso posterior na configuração do tempo de expiração dos tokens