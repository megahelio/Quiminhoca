import traceback
from fastapi import APIRouter, HTTPException
from models.formula_request import FormulaRequest
from utils.cache import get_cache_key
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
                        "source": "pubchem",
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

        cache_key = get_cache_key(req.formula.upper(), source)
        if redis_server and redis_server.exists(cache_key):
            source_results = json.loads(redis_server.get(cache_key).decode("utf-8"))
            cached = True
        else:
            source_results = source_func(req)
            if redis_server:
                redis_server.set(cache_key, json.dumps(source_results), ex=86400)
            cached = False
        results.append({
            "source": source,
            "cached": cached,
            "results": source_results
        })
    return results

def get_source_function(source: str):
    # Cada fuente debe tener un módulo llamado services.{source}_service y una función llamada query
    module_name = f"services.{source}_service"
    func_name = "query"
    try:
        logger.info(f"{source} {module_name} {func_name}")
        module = importlib.import_module(module_name)
        return getattr(module, func_name)
    except (ModuleNotFoundError, AttributeError) as e:
        logger.error(f"Error importando {module_name}.{func_name}: {e}")
        # logger.error(traceback.format_exc())
        raise HTTPException(status_code=400, detail=f"Fuente no soportada: {source}")
