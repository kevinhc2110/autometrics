import logging
import sys


def setup_logging(level: str = "INFO") -> None:
    """Configura el sistema de logging para la aplicación."""
    
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
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING) 
    
    # Logger para la aplicación
    logger = logging.getLogger("autometrics")
    logger.info("Sistema de logging configurado")
    
    return logger