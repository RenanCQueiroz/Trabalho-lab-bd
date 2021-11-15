


from fastapi import FastAPI
from schemas.index import unidade_bloco 
from routes.index import unidade_bloco
  
app = FastAPI()

app.include_router(unidade_bloco)
 




























