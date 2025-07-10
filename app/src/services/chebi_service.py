from requests import Response
from config import get_logger
from models.formula_request import FormulaRequest
from services.chebi_client import get_lite_entity

logger = get_logger(__name__)

def query(req: FormulaRequest):
    
    return get_lite_entity(req.formula)
    



