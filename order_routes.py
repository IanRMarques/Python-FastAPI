from fastapi import APIRouter

order_router = APIRouter(prefix='/pedidos', tags=['pedidos'])

@order_router.get('/')
async def get_orders():
    """Endpoint to retrieve orders."""
    return {'message': 'Rota de pedidos'}
    return {'message': 'Rota de pedidos'}
