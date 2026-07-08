from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

lista_clientes:list[Cliente]= []

#Crear el modelo clientes (id, nombre, correo, descripcion)
class Cliente(BaseModel):
    id: int
    nombre: str
    correo: str
    descripcion: str
#enpoint para listar clientes
@app.get("/clientes")
def listar_clientes():
    return lista_clientes

#endpoint para listar un solo cliente de la lista
@app.get("/clientes/{cliente_id}")
def listar_cliente(cliente_id: int):
    #recorrer la lista
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.get ("id") == cliente_id:
            return obj_cliente
    return lista_clientes

#endpoint para crear un cliente y agregar a la lista
@app.post("/clientes")
def crear_cliente(datos_cliente: Cliente):
    lista_clientes.append(datos_cliente)
    return datos_cliente