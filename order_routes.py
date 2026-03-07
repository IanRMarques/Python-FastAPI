from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from schemas import PedidoSchema
from models import Pedido, Usuario

order_router = APIRouter(prefix='/pedidos', tags=['pedidos'])

@order_router.get('/')
async def get_orders():
    """Endpoint to retrieve orders."""
    return {'message': 'Rota de pedidos'}



@order_router.post('/pedido')
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.id == pedido_schema.id_usuario).first()
    if (usuario is None):
        raise HTTPException(status_code=404, detail={'message': 'Usuário não encontrado, pedido não criado'})
    else:
        novo_pedido = Pedido(usuario=usuario.id)
        session.add(novo_pedido)
        session.commit()
        return {'message': 'Pedido criado com sucesso', 'id do pedido': novo_pedido.id}
    