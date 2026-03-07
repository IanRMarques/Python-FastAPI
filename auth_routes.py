from fastapi import APIRouter, Depends, HTTPException
from models import Usuario, db
from dependencies import bcrypt_context, ALGORITHM, SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, pegar_sessao
from schemas import LoginSchema, UserSchema
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone #importando classes para lidar com datas e horários, especialmente para configurar a expiração dos tokens de autenticação
auth_router = APIRouter(prefix='/auth', tags=['auth']) 

def criar_token(id_usuario):
    data_expiracao = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) #calculando a data de expiração do token, 
    #adicionando o tempo de expiração configurado (em minutos) à data e hora atual
    dic_info = {"sub": id_usuario, "exp": data_expiracao} #criando um dicionário com as informações a serem incluídas no token, como o ID do usuário e a data de expiração
    jwt_codificado = jwt.encode(dic_info, SECRET_KEY, ALGORITHM) #codificando o token usando a função encode da biblioteca jose, passando o dicionário de informações, a chave secreta e o algoritmo de criptografia configurados
    return jwt_codificado #retornando o token codificado, que pode ser usado para autenticação e autorização em rotas protegidas da API

def autenticar_usuario(email, senha, session):
    usuario = session.query(Usuario).filter(Usuario.email == email).first() #consultando o banco de dados para encontrar um usuário com o email fornecido
    if not usuario:
        return False #se o usuário não for encontrado, retornando False para indicar que a autenticação falhou
    elif not bcrypt_context.verify(senha, usuario.senha):#se o usuário for encontrado, verificando se a senha fornecida corresponde à senha armazenada no banco de dados usando o método verify do objeto bcrypt_context
        return False #se a senha não corresponder, retornando False para indicar que a autenticação falhou
    return usuario
   

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

#autenticação de login, verificando se o email existe e se a senha fornecida corresponde à senha armazenada no banco de dados para aquele email
#login - email e senha - token JWT (JSON Web Token) para autenticação e autorização em rotas protegidas
@auth_router.post('/login')
async def login(login_schema: LoginSchema, session: Session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(login_schema.email, login_schema.senha, session) #chamando a função autenticar_usuario para verificar as credenciais fornecidas e obter o usuário correspondente do banco de dados
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado ou credenciais invalidas") #se o usuário não for encontrado, levantando uma exceção HTTP com status 404 e uma mensagem de erro indicando que o usuário não foi encontrado
    else:
        access_token = criar_token(usuario.id) #criando um token de acesso usando a função criar_token, passando o ID do usuário encontrado
        return {
            "access_token": access_token, 
            "token_type": "bearer"
            } #retornando o token de acesso e o tipo de token como resposta da API, permitindo que o cliente use esse token para autenticação em rotas protegidas no futuro