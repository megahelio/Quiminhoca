from fastapi import APIRouter, HTTPException
from models.formula_request import FormulaRequest
from services.pubchem_service import query_pubchem_by_formula
from utils.cache import get_cache_key
from config import redis_server
import json

router = APIRouter()

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
    formula = req.formula.upper()
    source = req.sources[0]  # por ahora solo pubchem
    cache_key = get_cache_key(formula, source)

    if redis_server.exists(cache_key):
        return {"source": source, "cached": True, "results": json.loads(redis_server.get(cache_key).decode("utf-8"))}

    if source == "pubchem":
        results = query_pubchem_by_formula(formula)
    else:
        raise HTTPException(status_code=400, detail="Fuente no soportada")

    redis_server.set(cache_key, json.dumps(results), ex=86400)  # cachea por 1 día = 86400 segundos
    return {"source": source, "cached": False, "results": results}