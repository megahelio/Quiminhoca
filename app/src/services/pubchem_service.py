import time
from fastapi import HTTPException
import requests
from models.formula_request import FormulaRequest
from config import get_logger

logger = get_logger(__name__)

def get_results_by_listkey(listkey: str):
    properties = "IUPACName,MolecularFormula,MolecularWeight"
    output_format = "JSON"
    check_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/listkey/{listkey}/property/{properties}/{output_format}"
    
    max_wait = 5*4 
    interval = 1 
    elapsed = 0
    
    while elapsed < max_wait:
        response = requests.get(check_url)
        logger.debug(f"{response.status_code} {check_url}")
        if response.status_code == 200 or (response.status_code == 202 and 'PropertyTable' in response.json()):
            return response.json()['PropertyTable']['Properties']
        time.sleep(interval/4)
        elapsed += interval
    raise TimeoutError(f"No se completó en {max_wait}s")

def query(req: FormulaRequest):
    
    if isinstance(req.mass, float):
        cid_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/formula/{req.formula}/mass/{req.mass}/cids/JSON"
    else:
        cid_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/formula/{req.formula}/cids/JSON"
    
    response = requests.get(cid_url)
    
    logger.debug(f"Consultando PubChem por fórmula: {req.formula} -> ")
    logger.debug(f"{response.status_code} {cid_url} ")
    
    if response.status_code != 200 and response.status_code != 202:
        raise HTTPException(status_code=502, detail="Error consultando PubChem")
    
    if 'Waiting' in response.json():
        key = response.json()['Waiting']['ListKey']
        return get_results_by_listkey(key)
    
    elif 'PropertyTable' in response.json():
        return response.json()['PropertyTable']['Properties']
    
    else:
        raise ValueError("Respuesta no esperada: " + str(response.json()))