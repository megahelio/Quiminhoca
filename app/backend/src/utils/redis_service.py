from models.formula_request import FormulaRequest
import redis
from typing import Optional
from threading import Lock


class RedisService:
    _instance: Optional["RedisService"] = None
    _lock: Lock = Lock()

    def __init__(self, host="localhost", port=6379, db=0):
        if RedisService._instance is not None:
            raise Exception("Usa RedisService.get_instance()")
        self.client = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    @classmethod
    def get_instance(cls, host="localhost", port=6379, db=0) -> "RedisService":
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls(host, port, db)
        return cls._instance

    def get_client(self) -> redis.Redis:
        return self.client

    def set(self, key: str, value, expire: int = 86400):
        self.client.set(key, value, expire=expire)
    
    def set(self, req: FormulaRequest, source:str, value, expire: int = 86400) -> None:
        self.client.set(RedisService.get_key(req, source), value, expire)
        
    def get(self, key: str) -> Optional[str]:
        return self.client.get(key)
    
    def get(self, req: FormulaRequest, source: str) -> str:
        return self.client.get(RedisService.get_key(req, source))

    def delete(self, key: str):
        self.client.delete(key)

    def delete(self, req: FormulaRequest, source: str) -> str:
        return self.client.delete(RedisService.get_key(req, source))
    
    def ping(self):
        self.client.ping()

    @staticmethod
    def get_key(req: FormulaRequest, source: str):
        return f"{source}_{req.formula}".strip().lower().encode("utf-8")