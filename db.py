from pydantic import BaseModel

class Order(BaseModel):
    id: int
    fecha: str
    usuario: str
    tienda: str
    valor: float


ordenes = {
    1: Order(id=1, fecha="20-11-2020", usuario="pepe", tienda="dominos", valor=2000),
    2: Order(id=2, fecha="20-11-2020", usuario="juan", tienda="dominos", valor=3000),
}

def obtener_ordenes():
    #haga lo que tenga que hacer para conectarse a la base de datos
    lista_ordenes = []
    for e in ordenes:
        lista_ordenes.append(ordenes[e])
    return lista_ordenes