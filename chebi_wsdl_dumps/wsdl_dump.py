from zeep import Client
from datetime import datetime
from contextlib import redirect_stdout
from io import StringIO

wsdl_url = 'https://www.ebi.ac.uk/webservices/chebi/2.0/webservice?wsdl'
client = Client(wsdl=wsdl_url)

with StringIO() as buf:
    with redirect_stdout(buf):
        client.wsdl.dump()
    wsdl_output = buf.getvalue()

filename = f"chebi_wsdl_specs_dumps/chebi_wsdl_specs_dump_{datetime.now():%Y-%m-%d_%H-%M-%S}.txt"
with open(filename, 'w', encoding='utf-8') as f:
    f.write(wsdl_output)
print(f"Guardado en: {filename}")
