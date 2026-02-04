import logging
import sys
from typing import Any, Dict

def setup_logging(level: str = "INFO") -> None:
    """Configurar el sistema de logging"""
    
    # Configuración básica
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Configurar loggers específicos
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("fastapi").setLevel(logging.INFO)
    
    # Logger para la aplicación
    logger = logging.getLogger("autometrics")
    logger.info("Sistema de logging configurado")
    
    return logger