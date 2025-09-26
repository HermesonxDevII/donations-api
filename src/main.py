from fastapi import FastAPI
from . import models
from .database import engine

from .routers import users, companies, institutions, donations

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API REST para Doação de Alimentos",
    description="Este projeto implementa uma solução para conectar estabelecimentos doadores a ONGs e instituições sociais, permitindo o cadastro, consulta e gerenciamento de doações. [cite: 16, 17]",
    version="1.0.0",
    contact={
        "name": "Equipe de Desenvolvimento ADS",
        "url": "https://www.unifor.br",
    },
)

app.include_router(users.router, prefix="/users", tags=["Usuários e Autenticação"])
app.include_router(companies.router, prefix="/companies", tags=["Empresas Doadoras"])
app.include_router(institutions.router, prefix="/institutions", tags=["Instituições (ONGs)"])
app.include_router(donations.router, prefix="/donations", tags=["Doações"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API de Doação de Alimentos!"}