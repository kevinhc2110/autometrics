from datetime import datetime

from fastapi import APIRouter

from autometrics.core.config import settings

router = APIRouter()

@router.get("/health")
async def health_check():
    """Realiza una verificación de salud de la API"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": settings.VERSION,
        "environment": settings.ENV,
        "project_name": settings.PROJECT_NAME,
        "api_version": settings.API_V1_STR,
        "debug_mode": settings.DEBUG
    }

