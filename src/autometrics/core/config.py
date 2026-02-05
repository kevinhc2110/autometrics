import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuración de la aplicación."""

    load_dotenv()  # Cargar variables de entorno desde .env

    # Proyecto
    PROJECT_NAME = os.getenv("APP_NAME")
    VERSION = os.getenv("APP_VERSION")
    DESCRIPTION = os.getenv("APP_DESCRIPTION")
    
    # API
    API_V1_STR = os.getenv("API_V1_STR")
    
    # Entorno
    ENV = os.getenv("ENV")
    DEBUG = os.getenv("DEBUG")

    class Config:
        env_file = ".env"
        case_sensitive = True

# Instancia global de configuración
settings = Settings()