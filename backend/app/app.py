from backend.structure.df_creator import Frame
from backend.structure.data_collector import Collector
from fastapi import FastAPI
from backend.structure.base_model import ProcessamentoModel, ImportacaoModel, ExportacaoModel



app = FastAPI()
collect = Collector()


@app.get('/')
def route_default():
    return 'Welcome to my API'

@app.get('/producao')
async def get_full_production():
    urls = collect.get_producao()
    data = collect.get_full_data(urls)
    frame = Frame(data, collect.columns)
    
    return frame.get_json_data()

@app.get('/comercializacao')
async def get_full_commercialization():
    urls = collect.get_comercializacao()
    data = collect.get_full_data(urls)
    frame = Frame(data, collect.columns)
    
    return frame.get_json_data()

@app.get('/processamento')
async def get_full_processamento(subtype: ProcessamentoModel):
    if subtype is ProcessamentoModel.viniferas:
        urls = collect.get_processamento_viniferas()

    if subtype is ProcessamentoModel.americanas_hibridas:
        urls = collect.get_processamento_americanas_hibridas()

    if subtype is ProcessamentoModel.uva_mesa:
        urls = collect.get_processamento_uva_mesa()

    if subtype is ProcessamentoModel.sem_classificacao:
        urls = collect.get_processamento_sem_classificacao()

    data = collect.get_full_data(urls)
    frame = Frame(data, collect.columns)
    return frame.get_json_data()

@app.get('/importacao')
async def get_full_importacao(subtype: ImportacaoModel):
    if subtype is ImportacaoModel.vinho_mesa:
        urls = collect.get_importacao_vinho_mesa()

    if subtype is ImportacaoModel.espumante:
        urls = collect.get_importacao_espumante()

    if subtype is ImportacaoModel.uva_fresca:
        urls = collect.get_importacao_uva_fresca()

    if subtype is ImportacaoModel.uva_passa:
        urls = collect.get_importacao_uva_passa()

    if subtype is ImportacaoModel.suco_uva:
        urls = collect.get_importacao_suco_uva()

    data = collect.get_full_data(urls)
    frame = Frame(data, collect.columns)
    return frame.get_json_data()

@app.get('/exportacao')
async def get_full_exportacao(subtype: ExportacaoModel):
    if subtype is ExportacaoModel.vinho_mesa:
        urls = collect.get_exportacao_vinho_mesa()

    if subtype is ExportacaoModel.espumante:
        urls = collect.get_exportacao_espumante()

    if subtype is ExportacaoModel.uva_fresca:
        urls = collect.get_exportacao_uva_fresca()

    if subtype is ExportacaoModel.suco_uva:
        urls = collect.get_exportacao_suco_uva()

    data = collect.get_full_data(urls)
    frame = Frame(data, collect.columns)
    return frame.get_json_data()
