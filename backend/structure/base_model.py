from enum import Enum
from pydantic import BaseModel

class ProcessamentoModel(str, Enum):
    viniferas = 'viniferas'
    americanas_hibridas = 'americanas_hibridas'
    uva_mesa = 'uva_mesa'
    sem_classificacao = 'sem_classificacao'

class ImportacaoModel(str, Enum):
    vinho_mesa = 'vinho_mesa'
    espumante = 'espumante'
    uva_fresca = 'uva_fresca'
    uva_passa = 'uva_passa'
    suco_uva = 'suco_uva'

class ExportacaoModel(str, Enum):
    vinho_mesa = 'vinho_mesa'
    espumante = 'espumante'
    uva_fresca = 'uva_fresca'
    suco_uva = 'suco_uva'

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disable: str | None = None

class UserInDB(User):
    hashed_password: str