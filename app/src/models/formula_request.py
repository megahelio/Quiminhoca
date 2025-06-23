from pydantic import BaseModel, Field

class FormulaRequest(BaseModel):
    formula: str = Field(
        example="C6H12O6",
        description="Fórmula química molecular. Ej: C6H12O6 para glucosa."
    )
    sources: list[str] = Field(
        default=["pubchem"],
        example=["pubchem"],
        description="Lista de fuentes para buscar. Actualmente solo se soporta [PubChem](https://pubchem.ncbi.nlm.nih.gov/)."
    )