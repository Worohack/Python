# from /backend/FastAPI/fastapi import FastAPI

from fastapi import FastAPI
from enrutamientos import articulos, usuarios, autenticacion_basica
from fastapi.staticfiles import StaticFiles

mi_Api = FastAPI()

mi_Api.include_router(articulos.articulo)
mi_Api.include_router(usuarios.usuario)
mi_Api.include_router(autenticacion_basica.aut_basica)
mi_Api.mount("/recursos", StaticFiles(directory="recursos"), name="mis recursos")