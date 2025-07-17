from typing import Optional
from pydantic import BaseModel, Field
from models.sources_enum import SourceEnum

class FormulaRequest(BaseModel):
    formula: str = Field(
        examples=["C6H12O6", "H2O", "NaCl"],
        description="Fórmula química molecular. Ej: C6H12O6 para glucosa."
    )
    mass: Optional[float] = Field(
        default=None,
        description="Masa molecular (opcional)."
    )
    sources: list[SourceEnum] = Field(
        default=["PUBCHEM"],
        examples=[["PUBCHEM"], ["PUBCHEM", "CHEBI"]],
        description="Lista de fuentes para buscar. Actualmente solo se soporta [PubChem](https://pubchem.ncbi.nlm.nih.gov/)."
    )
