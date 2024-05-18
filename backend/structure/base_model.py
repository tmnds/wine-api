from enum import Enum


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
