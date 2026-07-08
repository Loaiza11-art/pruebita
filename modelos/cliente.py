from pydantic import BaseModel

#Crear el modelo clientes (id, nombre, correo, descripcion)
class ClienteBase(BaseModel):
    nombre: str
    correo: str
    descripcion: str

class ClienteCrear(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int |None = None

