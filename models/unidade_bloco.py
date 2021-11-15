from sqlalchemy import Table,Column
from config.db import meta
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.sqltypes import String


from config.db import meta

unidade_bloco = Table ( 
    "unidade_bloco", meta,
    Column('nome',String(255),primary_key=true)
)