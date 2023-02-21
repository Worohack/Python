from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

aut_basica = APIRouter(prefix="/autenticar")

'''
Como la clase de usuarios que se define abajo es la que se va a mover por toda la red, no se incluye la contraseña de acceso.
Ésta se puede obtener de una base de datos en la que está almacenada.
'''

class Usuarios(BaseModel):
    nombre_usuario: str
    nombre: str
    email: str
    activo: bool

class UsuariosBD(Usuarios):
    pasword: str

'''
Ahora voy a crear una falsa base de datos, ya que realmente es un diccionario en el que va a haber otro diccionario anidado.
'''

usuarios_bd = {
    "script": {
        "nombre_usuario": "script",
        "nombre": "Francisco J. Muñoz Ruano",
        "email": "ellaboratoriotecnologico@gmail.com",
        "activo": "True",
        "password": "123456"
    },
    "tampico": {
        "nombre_usuario": "tampico",
        "nombre": "Tampis Company",
        "email": "tampico@gmail.com",
        "activo": "False",
        "password": "789012"
    }
}

# Ahora defino la función de búsqueda que recibe como parámetro el nombre del usuario

def busca_usuario(nombre_usuario: str):
    # Pregunto si el usuario que le llega como parámetro a la función está en la base de datos

    if nombre_usuario in usuarios_bd:
        # Si existe, devuelve un objeto de la clase UsuariosBD con los datos del usuario encontrado
        
        return UsuariosBD(usuarios_bd[nombre_usuario])