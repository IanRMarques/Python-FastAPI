from models import db
from sqlalchemy.orm import sessionmaker #importando a classe sessionmaker do SQLAlchemy para criar sessões de banco de dados
from passlib.context import CryptContext
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def pegar_sessao():
    try:
        session = sessionmaker(bind=db) #criando uma classe de sessão vinculada ao engine do banco de dados
        session = session() #criando uma instância de sessão para interagir com o banco de dados
        yield session #utilizando yield para criar um gerador que retorna a sessão, permitindo que o FastAPI gerencie o ciclo de vida da sessão de forma eficiente
        session.close() #fechando a sessão após o uso 
    finally: #garantindo que aconteça caso de erro, sem tratamento de erros
         session.close()
