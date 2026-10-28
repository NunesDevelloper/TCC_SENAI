from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import route_manger

app = FastAPI(
    title="Api para o sistema da Lanchonete Sabor & Cia.",
    description="Sitema projetado para o gerenciamente de pedidos, estoques e fucionario para a aLanchonete Sabor & Cia.",
    version="0.0.1",
    contact={
        "name":"Suporte da API",
        "url": "https://github.com/NunesDevelloper/TCC_SENAI",
        "email": "arthurnunescarvalho2@gmail.com",
    },
    redoc_url=None
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(route_manger.mr)