from models import db
from sqlalchemy.orm import sessionmaker #importando a classe sessionmaker do SQLAlchemy para criar sessões de banco de dados
def pegar_sessao():
    session = sessionmaker(bind=db) #criando uma classe de sessão vinculada ao engine do banco de dados
    session = session() #criando uma instância de sessão para interagir com o banco de dados

    return session