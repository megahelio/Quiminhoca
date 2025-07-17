from pydantic import BaseModel
class FormulaResponse(BaseModel):
    name: str
    id: int
    source: str