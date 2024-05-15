from fastapi import FastAPI

from utils.structure.data_functions import get_data

app = FastAPI()

@app.get('/')
def get_home():
    return {'hello': 'world'}

@app.get('/producao')
def get_producao():
    data = get_data()
    return data