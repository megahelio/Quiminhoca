import os
import redis
# Configuración de Redis (usa variables de entorno o valores por defecto)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))

# Conexión a Redis
redis_server = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

# Configuración de logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
