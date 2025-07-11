import os
import redis
import logging
import sys

LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG").upper()
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

def get_logger(name="app"):
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, LOG_LEVEL, logging.DEBUG))

    if not logger.hasHandlers():
        formatter = logging.Formatter(LOG_FORMAT)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

logger = get_logger(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))

# Conexión a Redis
try:
    redis_server = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    redis_server.ping()
    logger.info("Conexión a Redis establecida.")
except (redis.exceptions.ConnectionError, redis.exceptions.TimeoutError) as e:
    logger.warning("Funcionando sin caché de Redis")
    logger.debug(f"No se pudo conectar a Redis: {e}")
    redis_server = None 



