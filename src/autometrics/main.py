from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from autometrics.api.v1 import health, root, routes
from autometrics.core.config import settings
from autometrics.core.logging import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Código de inicio
    logger = setup_logging()
    logger.info("Iniciando aplicación AutoMetrics")
    yield
    # Código de cierre
    logger.info("Cerrando aplicación AutoMetrics")

# Crear aplicación FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
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
app.include_router(health.router, prefix=settings.API_V1_STR, tags=["health"])
app.include_router(routes.router, prefix=settings.API_V1_STR, tags=["routes"])
app.include_router(root.router, tags=["root"])

