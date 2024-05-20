from fastapi import FastAPI

from backend.structure.df_creator import Frame
from backend.structure.data_collector import Collector
from backend.structure.base_model import ProcessamentoModel, ImportacaoModel, ExportacaoModel



app = FastAPI()
collect = Collector()


@app.get('/')
def route_default():
    return 'Welcome to my API'

@app.get('/producao/{year}')
async def get_production(year):
    urls = collect.get_simple_url(year, 'producao')
    data = collect.get_data(urls)
    frame = Frame(data, collect.columns)
    
    return frame.get_json_data()

@app.get('/producao')
async def get_full_production():
    urls = collect.get_full_simple_url('producao')
    data = collect.get_full_data(urls)
    frame = Frame(data, collect.columns)
    
    return frame.get_json_data()

@app.get('/comercializacao')
async def get_full_commercialization():
    urls = collect.get_full_simple_url('comercializacao')
    data = collect.get_full_data(urls)
    frame = Frame(data, collect.columns)
    
    return frame.get_json_data()

@app.get('/processamento')
async def get_full_processamento(subtype: ProcessamentoModel):
    if subtype is ProcessamentoModel.viniferas:
        urls = collect.get_full_complex_url('processamento', subtype)

    if subtype is ProcessamentoModel.americanas_hibridas:
        urls = collect.get_full_complex_url('processamento', subtype)

    if subtype is ProcessamentoModel.uva_mesa:
        urls = collect.get_full_complex_url('processamento', subtype)

    if subtype is ProcessamentoModel.sem_classificacao:
        urls = collect.get_full_complex_url('processamento', subtype)

    data = collect.get_full_data(urls)
    frame = Frame(data, collect.columns)
    return frame.get_json_data()

@app.get('/importacao')
async def get_full_importacao(subtype: ImportacaoModel):
    if subtype is ImportacaoModel.vinho_mesa:
        urls = collect.get_full_complex_url('importacao', subtype)

    if subtype is ImportacaoModel.espumante:
        urls = collect.get_full_complex_url('importacao', subtype)

    if subtype is ImportacaoModel.uva_fresca:
        urls = collect.get_full_complex_url('importacao', subtype)

    if subtype is ImportacaoModel.uva_passa:
        urls = collect.get_full_complex_url('importacao', subtype)

    if subtype is ImportacaoModel.suco_uva:
        urls = collect.get_full_complex_url('importacao', subtype)

    data = collect.get_full_data(urls)
    frame = Frame(data, collect.columns)
    return frame.get_json_data()

@app.get('/exportacao')
async def get_full_exportacao(subtype: ExportacaoModel):
    if subtype.name == 'vinho_mesa':
        urls = collect.get_full_complex_url('exportacao', 'vinho_mesa')

    if subtype.name == 'espumante':
        urls = collect.get_full_complex_url('exportacao', 'espumante')

    if subtype is ExportacaoModel.uva_fresca:
        urls = collect.get_full_complex_url('exportacao', subtype)

    if subtype is ExportacaoModel.suco_uva:
        urls = collect.get_full_complex_url('exportacao', subtype)

    data = await collect.get_full_data(urls)
    frame = Frame(data, collect.columns)
    return frame.get_json_data()
