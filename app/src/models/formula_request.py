from typing import Optional
from pydantic import BaseModel, Field

class FormulaRequest(BaseModel):
    formula: str = Field(
        examples=["C6H12O6", "H2O", "NaCl"],
        description="Fórmula química molecular. Ej: C6H12O6 para glucosa."
    )
    mass: Optional[float] = Field(
        default=None,
        description="Masa molecular (opcional)."
    )
    sources: list[str] = Field(
        default=["pubchem"],
        examples=[["pubchem"], ["pubchem", "other_source"]],
        description="Lista de fuentes para buscar. Actualmente solo se soporta [PubChem](https://pubchem.ncbi.nlm.nih.gov/)."
    )
