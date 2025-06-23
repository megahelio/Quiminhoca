import time
from fastapi import HTTPException
import requests
import logging

# Configuración de logging
logger = logging.getLogger(__name__)

def query_pubchem_by_listkey(listkey: str):
    properties = "IUPACName,MolecularFormula,MolecularWeight"
    output_format = "JSON"
    check_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/listkey/{listkey}/property/{properties}/{output_format}"
    
    max_wait = 60
    interval = 2
    elapsed = 0
    while elapsed < max_wait:
        response = requests.get(check_url)
        if response.status_code == 200 or (response.status_code == 202 and 'PropertyTable' in response.json()):
            return response.json()['PropertyTable']['Properties']
        time.sleep(interval)
        elapsed += interval
    raise TimeoutError(f"No se completó en {max_wait}s")

def query_pubchem_by_formula(formula: str):
    cid_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/formula/{formula}/cids/JSON"
    resp = requests.get(cid_url)
    logger.debug(f"Consultando PubChem por fórmula: {formula} -> {cid_url}")
    logger.debug(f"Obtenido: {resp}")
    if resp.status_code != 200 and resp.status_code != 202:
        raise HTTPException(status_code=502, detail="Error consultando PubChem")
    if 'Waiting' in resp.json():
        key = resp.json()['Waiting']['ListKey']
        return query_pubchem_by_listkey(key)
    elif 'PropertyTable' in resp.json():
        return resp.json()['PropertyTable']['Properties']
    else:
        raise ValueError("Respuesta no esperada: " + str(resp.json()))