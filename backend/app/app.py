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
    urls = collect.get_full_complex_url('processamento', subtype)
    data = collect.get_full_data(urls)
    frame = Frame(data, collect.columns)
    
    return frame.get_json_data()

@app.get('/importacao')
async def get_full_importacao(subtype: ImportacaoModel):
    urls = collect.get_full_complex_url('importacao', subtype)
    data = collect.get_full_data(urls)
    frame = Frame(data, collect.columns)
    
    return frame.get_json_data()

@app.get('/exportacao')
async def get_full_exportacao(subtype: ExportacaoModel):
    urls = collect.get_full_complex_url('exportacao', subtype)
    data = collect.get_full_data(urls)
    frame = Frame(data, collect.columns)
    
    return frame.get_json_data()
