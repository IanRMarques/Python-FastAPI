from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

dp = create_engine("sqlite:///.database.db")    

#cria a base do bd
Base = declarative_base()

#cria as classes/tabelas do bd
#usuario, pedidos, itenspedidos
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(100), nullable=False)
    ativo = Column(Boolean, default=True)
    admin = Column(Boolean, default=False)

# executa a criação dos metadados (tabelas) no banco de dados 