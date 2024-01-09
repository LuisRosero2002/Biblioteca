from pydantic import BaseModel
from typing import Optional

class LibroSchema(BaseModel):
    # id: Optional[int] = None
    titulo: str
    autor:int
    genero:int
    anio:int