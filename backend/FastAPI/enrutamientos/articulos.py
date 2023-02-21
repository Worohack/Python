from fastapi import APIRouter

articulo = APIRouter(prefix="/articulo", tags = ["Artículos"], responses={404:{"mensaje":"No encontrado"}})
lista_articulos = [{"Codigo": 1, "Descripción": "Sombrero", "Precio": 23.00}, 
                    {"Codigo": 2, "Descripción": "Gorra", "Precio": 12.00},
                    {"Codigo": 3, "Descripción": "Guantes", "Precio": 30.00}]

@articulo.get("/")
async def lista_articulo():
    return lista_articulos