# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api import router as api_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="Task Manager Advanced",
        description="Gerenciador de tarefas com FastAPI, Celery, Redis e PostgreSQL.",
        version="1.0.0"
    )

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Troque por domínios específicos em produção
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Endpoint de healthcheck
    @app.get("/health")
    def health():
        return {"status": "ok"}

    # Rota raiz simples para teste
    @app.get("/")
    def root():
        return {"message": "API rodando!"}

    # Rotas principais
    app.include_router(api_router)

    return app

app = create_app()
