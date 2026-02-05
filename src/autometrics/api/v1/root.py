import logging

from fastapi import APIRouter

from autometrics.core.config import settings

logger = logging.getLogger("autometrics")
router = APIRouter()

# Ruta raíz
@router.get("/")
async def root():
    """Indica la información básica de la API"""
    return {
        "message": "Welcome to AutoMetrics",
        "version": settings.VERSION,
        "docs": "/docs",
        "health": "/api/v1/health"
    }