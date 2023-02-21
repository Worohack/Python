from fastapi import APIRouter
from pydantic import BaseModel

class Clase_Usuario(BaseModel):
    nombre: str
    apellidos: str
    url: str
    edad: int

usuario = APIRouter(prefix="/usuario", tags = ["Usuarios"], responses={404:{"mensaje":"No encontrado"}})
@usuario.get("/users/")
async def users():
    return "Hola usuario"


lista_usuario = [Clase_Usuario(nombre = "Luís", apellidos = "Sierra González", url = "sierrag.com", edad = 20),  
                    Clase_Usuario(nombre = "Rafael", apellidos = "Vargas Ruano", url = "vargasr.com", edad = 29), 
                    Clase_Usuario(nombre = "Mario", apellidos = "Muñoz Ruíz", url = "munozr.es", edad = 35)]

@usuario.get("/")
async def muestra_usuario():
    return lista_usuario

@usuario.get("/{identificador}")
async def un_usuario(identificador: int):
    resultado = filter(lambda un_usuario: un_usuario.id == identificador, lista_usuarios)
    try:
        return list(resultado)[0]
    except:
        return {"Error:": "No se encuentra el usuario"}

@usuario.get("/")
async def usuario_con_query(identificador: int):
    resultado = filter(lambda un_usuario: un_usuario.id == identificador, lista_usuario)
    try:
        return list(resultado)[0]
    except:
        return {"Error:": "No se encuentra el usuario"}



@usuario.post("/")
#########################################################################
# Pasamos como parámetro un nuevo objeto (mi_nuevo_usuario) de la clase #
# Clase_Usuario                                                         #
#########################################################################
async def crea_usuario(mi_nuevo_usuario: Clase_Usuario):
####################################################################################
# Comprobamos que realmente lo que recibimos es un objeto de tipo Clase_Usuario    #
# después de ejecutar la función "busca", y si es así, se muestra un error         #
# indicando que ya existe el usuario; en caso contrario, se guarda en la lista     #
# el nuevo usuario.                                                                #
####################################################################################
    if type(busca(mi_nuevo_usuario.id)) == Clase_Usuario:
        return {"Error": "El usuario ya existe"}
    else:
        lista_usuario.append(mi_nuevo_usuario)
        return mi_nuevo_usuario
    
@usuario.put("/")

################################################################################
# Pasamos como parámetro un nuevo objeto (usuario_para_actualizar) de la clase #
# Clase_Usuario                                                                #
################################################################################
async def modifica_usuario(usuario_para_actualizar: Clase_Usuario):
#####################################################################################
# Como estamos trabajando con una lista en la que están almacenados los usuarios,   #
# recorremos toda la lista con un for; además, como necesitamos saber el índice     #
# del elemento de la lista, la convertimos en un enumerador y en el mismo for       #
# obtenemos el índice.                                                              #
#####################################################################################
   for index, usuario_guardado in enumerate(lista_usuario):
 	   if usuario_guardado.id == usuario_para_actualizar.id:
            lista_usuario[index] = usuario_para_actualizar
            return usuario_para_actualizar

@usuario.delete("/{id}")
async def borrado(id: int): # El nombre del parámetro debe ser igual al que se ha puesto en el path (En este caso "id")
    for indice, usuario_borrado in enumerate(lista_usuario): 
        if usuario_borrado.id == id:
            del lista_usuario[indice]


def busca(mi_id):
    resultado = filter(lambda un_usuario: un_usuario.id == mi_id, lista_usuario)
    try:
        return list(resultado)[0]
    except:
        return {"Error:": "No se encuentra el usuario"}


