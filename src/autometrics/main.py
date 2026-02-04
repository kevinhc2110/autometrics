from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from autometrics.api.v1 import health, routes
from autometrics.core.config import settings
from autometrics.core.logging import setup_logging

# Configurar logging
setup_logging()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print(f"🚀 Iniciando {settings.PROJECT_NAME}...")
    yield
    # Shutdown
    print("🛑 Cerrando aplicación...")

# Crear aplicación FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Automated metrics dashboard using FastAPI, n8n and AI",
    version="0.1.0",
    lifespan=lifespan
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(routes.router, prefix="/api/v1", tags=["routes"])

# Ruta raíz
@app.get("/")
async def root():
    return {
        "message": "Welcome to AutoMetrics API",
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/api/v1/health"
    }