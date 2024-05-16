from backend.structure.df_creator import Frame
from backend.structure.data_collector import Collector
from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def route_default():
    return 'Welcome to my API'

@app.get('/producao')
def get_full_production():
    collect = Collector()
    urls = collect.get_producao()
    data = collect.get_full_data(urls)
    frame = Frame(data, collect.columns)
    
    return frame.get_json_data()

@app.get('/comercializacao')
def get_full_commercialization():
    collect = Collector()
    urls = collect.get_comercializacao()
    data = collect.get_full_data(urls)
    frame = Frame(data, collect.columns)
    
    return frame.get_json_data()