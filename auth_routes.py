from fastapi import APIRouter, Depends
from models import Usuario, db
from dependencies import pegar_sessao

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.get('/')
async def home():
    """Our system's authentication endpoint."""
    return {'message': 'Rota de autenticação', "autenticação":False}
#criar rota para criar usuario.
@auth_router.post('/create_user')
#criando a função para criar um usuario, recebendo email e senha como parâmetros, e utilizando a classe Usuario do models para criar um novo usuário no banco de dados
async def create_user(email: str,senha: str, nome:str, session = Depends(pegar_sessao)):
    #verificando se o email já existe.
    usuario = session.query(Usuario).filter(Usuario.email == email).first() #consultando o banco de dados para verificar se já existe um usuário com o email fornecido
    if usuario:
        return {'message': 'Email já cadastrado'}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario) #adicionando o novo usuário à sessão
        session.commit() #confirmando a transação para salvar o novo usuário no banco de dados
        return {'message': 'Usuário criado com sucesso', 'nome': nome, 'email': email}
