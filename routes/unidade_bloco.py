from sqlalchemy.sql.sqltypes import String
from fastapi import APIRouter
from config.db import conn
from models.index import unidade_bloco
from schemas.index import unidade_bloco

# unidade_bloco = unidade/bloco na documentacao eu decidi mudar a barra por um underline para minimizar o risco de dar erros com encoding


unidade_bloco = APIRouter() 

@unidade_bloco.get("/")
async def read_data():
    return conn.execute(unidade_bloco.select()).fetchall()


@unidade_bloco.get("/{nome}")
async def read_data(nome : str):
    return conn.execute(unidade_bloco.select().where(unidade_bloco.c.nome == nome)).fetchall()

"""
@unidade_bloco.post("/") #acho que nao precisa desse nome
async def write_data(unidade_bloco: unidade_bloco): #o problema esta no unidade_bloco sendo hasheado,alterar o model e schema dele para achar a fonte do problema
    conn.execute(unidade_bloco.insert().values( 
        nome=unidade_bloco.nome
    ))

    return conn.execute(unidade_bloco.select()).fetchall()



@unidade_bloco.put("/{nome}")
async def update_data(nome : str,unidade_bloco : unidade_bloco):
    conn.execute(unidade_bloco.update().values(
        nome=unidade_bloco.nome
    ).where(unidade_bloco.c.nome == nome))
    return conn.execute(unidade_bloco.select()).fetchall()
"""

@unidade_bloco.delete("/{nome}") 
async def delete_data(nome : str):
    conn.execute(unidade_bloco.delete().where(unidade_bloco.c.nome == nome))
    return conn.execute(unidade_bloco.select()).fetchall()   


