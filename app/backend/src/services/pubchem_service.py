import json
import time
import requests
from fastapi import HTTPException
from models.sources_enum import SourceEnum
from utils.redis_service import RedisService
from models.formula_request import FormulaRequest
from config import get_logger

logger = get_logger(__name__)

class PubchemService:
    BASE_URL = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
    PROPERTIES = "IUPACName,MolecularFormula,MolecularWeight"
    OUTPUT_FORMAT = "JSON"
    TIMEOUT = 20
    INTERVAL = 1
    @staticmethod
    def get_results_by_listkey(listkey: str):
        check_url = f"{PubchemService.BASE_URL}/compound/listkey/{listkey}/property/{PubchemService.PROPERTIES}/{PubchemService.OUTPUT_FORMAT}"
        elapsed = 0

        while elapsed < PubchemService.TIMEOUT:
            response = requests.get(check_url)
            logger.debug(f"{response.status_code} {check_url}")

            if response.status_code == 200 and 'PropertyTable' in response.json():
                return response.json()['PropertyTable']['Properties']
            
            time.sleep(PubchemService.INTERVAL)
            elapsed += PubchemService.INTERVAL

        raise TimeoutError(f"No se completó en {PubchemService.TIMEOUT}s")
    
    @staticmethod
    def query(req: FormulaRequest):
        cached = RedisService.get_instance().get(req,  SourceEnum.PUBCHEM.value)
        if cached:
            return json.loads(cached)
        
        if isinstance(req.mass, float):
            cid_url = f"{PubchemService.BASE_URL}/compound/formula/{req.formula}/mass/{req.mass}/cids/{PubchemService.OUTPUT_FORMAT}"
        else:
            cid_url = f"{PubchemService.BASE_URL}/compound/formula/{req.formula}/cids/{PubchemService.OUTPUT_FORMAT}"

        response = requests.get(cid_url)
        
        logger.debug(f"Consultando PubChem por fórmula: {req.formula}")
        logger.debug(f"{response.status_code} {cid_url}")

        if response.status_code not in (200, 202):
            raise HTTPException(status_code=502, detail="Error consultando PubChem")

        json_data = response.json()

        if 'Waiting' in json_data:
            response = PubchemService.get_results_by_listkey(json_data['Waiting']['ListKey'])
            RedisService.get_instance().set(req, SourceEnum.PUBCHEM.value, json.dumps(response), expire=3600)
            return response
        
        elif 'PropertyTable' in json_data:
            RedisService.get_instance().set(req, SourceEnum.PUBCHEM.value, json_data['PropertyTable']['Properties'], expire=3600)
            return json_data['PropertyTable']['Properties']
        
        else:
            raise ValueError("Respuesta no esperada: " + str(json_data))
