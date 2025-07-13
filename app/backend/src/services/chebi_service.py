import json
from config import get_logger
from models.formula_request import FormulaRequest
from utils.chebi_client import get_lite_entity
from utils.redis_service import RedisService
from models.formula_response import FormulaResponse
from models.sources_enum import SourceEnum
from zeep.helpers import serialize_object

logger = get_logger(__name__)

class ChebiService:
    @staticmethod
    def query(req: FormulaRequest)-> list[FormulaResponse]:
        cached = RedisService.get_instance().get(req,  SourceEnum.CHEBI.value)
        
        if cached:
            return json.loads(cached)
        
        data = [serialize_object(lite_entity) for lite_entity in get_lite_entity(req.formula)]
        RedisService.get_instance().set(req, SourceEnum.CHEBI.value, json.dumps(data), expire=3600)
        return data
    



