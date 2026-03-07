from fastapi import APIRouter, Depends, HTTPException
from models import Usuario, db
from dependencies import pegar_sessao
from dependencies import bcrypt_context
from schemas import UserSchema
from sqlalchemy.orm import Session


auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.get('/')
async def home():
    """Our system's authentication endpoint."""
    return {'message': 'Rota de autenticação', "autenticação":False}


#criar rota para criar usuario.
@auth_router.post('/create_user')
#criando a função para criar um usuario, recebendo email e senha como parâmetros, e utilizando a classe Usuario do models para criar um novo usuário no banco de dados
async def create_user(usuario_schema: UserSchema, session = Depends(pegar_sessao)):
    #verificando se o email já existe.
    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first() #consultando o banco de dados para verificar se já existe um usuário com o email fornecido
    if usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado") #usa raise para retornar um erro
        #se o email já estiver cadastrado, levantando uma exceção HTTP com status 400 e uma mensagem de erro indicando que o email já está em uso
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha) #criptografando a senha fornecida usando o objeto bcrypt_context configurado para usar o algoritmo bcrypt
        novo_usuario = Usuario(nome=usuario_schema.nome, email=usuario_schema.email, senha=senha_criptografada, ativo=usuario_schema.ativo, admin=usuario_schema.admin) 
        #criando uma nova instância da classe Usuario com o nome, email e senha criptografada fornecidos
        session.add(novo_usuario) #adicionando o novo usuário à sessão
        session.commit() #confirmando a transação para salvar o novo usuário no banco de dados
        return {'message': f'Usuário criado com sucesso', 'nome': usuario_schema.nome, 'email': usuario_schema.email}
