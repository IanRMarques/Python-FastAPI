import token

from models import db
from sqlalchemy.orm import sessionmaker, Session #importando a classe sessionmaker do SQLAlchemy para criar sessões de banco de dados
from passlib.context import CryptContext
import os
from models import Usuario
from fastapi import Depends, HTTPException #importando a função Depends do FastAPI para gerenciar dependências, permitindo que as rotas e funções dependam de outras funções ou recursos, como sessões de banco de dados ou autenticação
from jose import jwt, JWTError
from main import oauth2_schema
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


def verificar_token(token: str = Depends(oauth2_schema), session: Session = Depends(pegar_sessao)): #definindo a função verificar_token, que é usada para verificar a validade de um token de autenticação fornecido pelos clientes,
#recebendo o token como uma string e a sessão do banco de dados como dependências, permitindo que o FastAPI gerencie a injeção dessas dependências quando a função for chamada em rotas protegidas
    try:
        dic_info = jwt.decode(token, SECRET_KEY, ALGORITHM) #decodificando o token usando a função decode da biblioteca jose, passando o token, a chave
        id_usuario = dic_info.get("sub") #extraindo o ID do usuário do dicionário de informações decodificado, usando a chave "sub" que foi definida ao criar o token (auth_routes.py, linha 15)   
    except JWTError:
         raise HTTPException(status_code=401, detail="Acesso negado, verifique a validade do token") #se a decodificação falhar, levantando uma exceção HTTP com status 401 e uma mensagem de erro indicando que o token é inválido
    #verificar se o token é valido e extrair o ID do usuário
    usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first() #consultando o banco de dados para encontrar um usuário com o ID extraído do token
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado") #se o usuário não for encontrado, levantando uma exceção HTTP com status 404 e uma mensagem de erro indicando que o usuário não foi encontrado
    return usuario  
