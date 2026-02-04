from fastapi import APIRouter
from datetime import datetime
from autometrics.core.config import settings

router = APIRouter()

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": settings.VERSION,
        "environment": settings.ENV
    }

@router.get("/health/detailed")
async def detailed_health_check():
    """Detailed health check with more information"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": settings.VERSION,
        "environment": settings.ENV,
        "project_name": settings.PROJECT_NAME,
        "api_version": settings.API_V1_STR,
        "debug_mode": settings.DEBUG
    }