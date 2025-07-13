from typing import Callable
from models.sources_enum import SourceEnum
from fastapi import APIRouter, HTTPException
from models.formula_request import FormulaRequest
from utils.redis_service import RedisService
from config import redis_server, get_logger
import importlib
import json

router = APIRouter()

logger = get_logger(__name__)

@router.post(
    "/lookup",
    summary="Buscar compuestos por fórmula química",
    description="Consulta bases de datos químicas públicas para obtener información sobre compuestos a partir de su fórmula molecular.",
    responses={
        200: {
            "description": "Consulta exitosa",
            "content": {
                "application/json": {
                    "example": {
                        "source": "PUBCHEM",
                        "cached": False,
                        "results": [
                            {
                                "cid": 5793,
                                "MolecularFormula": "C6H12O6",
                                "MolecularWeight": 180.15588,
                                "IUPACName": "(2R,3R,4R,5R)-2,3,4,5,6-pentahydroxyhexanal",
                                "image": "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/5793/PNG"
                            }
                        ]
                    }
                }
            }
        },
        502: {"description": "Error consultando la API externa (PubChem)"},
        400: {"description": "Fuente no soportada aún"}
    })
def lookup_formula(req: FormulaRequest):
    logger.debug(f"Request: {vars(req)}")
    results = []
    for source in req.sources:
        source_func = get_source_function(source)
        
        source_results = source_func(req)
           
        results.append({
            "source": source,
            "results": source_results
        })
    return results

def get_source_function(source: SourceEnum) -> Callable:
    module_name = f"services.{source.value.lower()}_service"
    class_name = f"{source.value.capitalize()}Service"
    try:
        module = importlib.import_module(module_name)
        service_class = getattr(module, class_name)
        return service_class.query

    except (ModuleNotFoundError, AttributeError) as e:
        logger.error(f"Error importando {module_name}.{class_name}.query: {e}")
        raise HTTPException(status_code=400, detail=f"Fuente no soportada: {source}")

