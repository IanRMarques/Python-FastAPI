#usado para forçar a tipagem dos dados, garantindo que as informações sejam do tipo esperado e facilitando a validação e manipulação dos dados recebidos nas rotas da API
from pydantic import BaseModel 
from typing import Optional #importando a classe optional para passar diferente dos basicos

class UserSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool] = True #definindo o campo ativo como opcional, com um valor padrão de True, indicando que o usuário está ativo por padrão, mas permitindo que seja definido como False se necessário
    admin: Optional[bool] = False #definindo o campo admin como opcional, com um valor padrão de False, indicando que o usuário não é um administrador por padrão, mas permitindo que seja definido como True se necessário

    class Config:
        from_attributes = True #configurando a classe para permitir a criação de instâncias do modelo a partir de objetos que possuem atributos correspondentes, 
        #facilitando a integração com outros tipos de dados e bibliotecas que possam retornar objetos em vez de dicionários

class PedidoSchema(BaseModel):
    id_usuario: int

    class Config:
        from_attributes = True

class LoginSchema(BaseModel):
    email: str
    senha: str

    class Config:
        from_attributes = True
