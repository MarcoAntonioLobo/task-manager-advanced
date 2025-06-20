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

    # Configuração CORS - ajuste allow_origins para produção
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Em produção, especifique os domínios permitidos
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Endpoint simples para healthcheck
    @app.get("/health")
    def health():
        return {"status": "ok"}

    # Rota raiz para verificação rápida
    @app.get("/")
    def root():
        return {"message": "API rodando!"}

    # Inclui rotas da aplicação principal
    app.include_router(api_router)

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
