from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Proyecto
    PROJECT_NAME: str = "AutoMetrics"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "Automated metrics dashboard using FastAPI, n8n and AI"
    
    # API
    API_V1_STR: str = "/api/v1"
    
    # Base de datos
    DATABASE_URL: Optional[str] = None
    
    # OpenAI
    OPENAI_API_KEY: Optional[str] = None
    
    # Entorno
    ENV: str = "development"
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Instancia global de configuración
settings = Settings()