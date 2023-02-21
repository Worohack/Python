from fastapi import FastAPI
from pydantic import BaseModel

usuario = FastAPI()
@usuario.get("/users")
async def users():
    return "Hola usuario"