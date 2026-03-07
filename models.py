from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Float, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType

db = create_engine("sqlite:///.database.db")    

#cria a base do bd
Base = declarative_base()

#cria as classes/tabelas do bd
#usuario, pedidos, itenspedidos
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column("id",Integer, primary_key=True, autoincrement=True)
    nome = Column("nome",String(50), nullable=False)
    email = Column("email",String(100), unique=True, nullable=False)
    senha = Column("senha",String(100), nullable=False)
    ativo = Column("ativo",Boolean, default=True)
    admin = Column("admin",Boolean, default=False)

    #construtor da classe
    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class Pedido(Base):
    __tablename__ = 'pedidos'
    #criação de uma tupla para os status dos pedidos, utilizando o ChoiceType do SQLAlchemy para garantir que apenas valores válidos sejam atribuídos ao campo "status"
    #Status_pedidos = (
     #   ("Pendente", "Pendente"),
    #    ("Concluído", "Concluído"),
   #    ("Cancelado", "Cancelado")
  #  ) Erro por conta do alempic, não aceita com o sqlalchemy utils
    id = Column("id",Integer, primary_key=True, autoincrement=True)
    status = Column("status",String, nullable=False) #utilização do ChoiceType para o campo "status"
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float,nullable=False)

    #construtor da classe
    def __init__(self, status="Pendente", usuario=None, preco=0.0):
        self.status = status
        self.preco = preco
        self.usuario = usuario

class ItemPedido(Base):
    __tablename__= "itens_pedidos"
    
    id = Column("id",Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer, nullable=False) #nullable serve para informar que não pode ser nulo o campo
    sabor = Column("sabor", String(50), nullable=False)
    tamanho = Column("tamanho", String(20), nullable=False)
    preco_unitario = Column("preco_unitario", Float,nullable=False)
    pedido = Column("pedido", ForeignKey("pedidos.id")) #chave estrangeira para relacionar o item ao pedido
     
    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido


# executa a criação dos metadados (tabelas) no banco de dados 
