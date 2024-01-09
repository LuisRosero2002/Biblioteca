from pydantic import BaseModel
from typing import Optional

class UsuariosSchema(BaseModel):
    # id: Optional[int] = None
    usuario: str
    contrasena: str