from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.get('/')
async def auth():
    """Our system's authentication endpoint."""
    return {'message': 'Rota de autenticação'}

