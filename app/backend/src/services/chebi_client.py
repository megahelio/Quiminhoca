from xmlrpc.client import Fault
from zeep import Client
from config import get_logger

logger = get_logger(__name__)

wsdl_url = 'https://www.ebi.ac.uk/webservices/chebi/2.0/webservice?wsdl'
client = Client(wsdl=wsdl_url)


# Acceder a los tipos definidos en el WSDL
search_type_enum = client.get_type("ns0:SearchCategory")
stars_category_enum = client.get_type("ns0:StarsCategory")

def get_lite_entity(formula):
    try:
        # Ejecutar búsqueda estructural (por fórmula)
        result = client.service.getLiteEntity(
            search=formula,
            searchCategory=search_type_enum("ALL"),
            stars=stars_category_enum("ALL"),  
            maximumResults=20,
        )
        return result

    except Fault as fault:
        logger.error(f"Error SOAP: {fault}")



