from fastapi import FastAPI, Path, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
 

from backend.structure.df_creator import Frame
from backend.structure.data_collector import Collector
from backend.structure.base_model import ProcessamentoModel, ImportacaoModel, ExportacaoModel, User


app = FastAPI()
collect = Collector()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


#Auth

def fake_decode_token(token):
    return User(
        username=token + 'fakedecoded', email='myemail.example.com', full_name='Thales Mendes'
    )

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user

#Teste auth

@app.get('/users/me')
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user

# default code
@app.get('/')
def route_default():
    return 'Welcome to API Embrapa'

# Get Year data

@app.get('/producao/{year}/token')
async def get_production(
    year: Annotated[int, Path(title="The ID of the item to get", ge=1970, le=2022)],
    token: Annotated[str, Depends(oauth2_scheme)]
    
):

    urls = collect.get_simple_url(year, 'producao')
    data = collect.get_data(urls, year)
    frame = Frame(data, collect.columns)
    
    # return 
    return {'token': token}

@app.get('/comercializacao/{year}')
async def get_commercialization(
    year: Annotated[int, Path(title="The ID of the item to get", ge=1970, le=2022)]
):

    urls = collect.get_simple_url(year, 'comercializacao')
    data = collect.get_data(urls, year)
    frame = Frame(data, collect.columns)
    
    return frame.get_json_data()

@app.get('/processamento/{year}')
async def get_processamento(
    year: Annotated[int, Path(title="The ID of the item to get", ge=1970, le=2022)], 
    subtype: ProcessamentoModel
):
    urls = collect.get_complex_url(year, 'processamento', subtype)
    data = collect.get_data(urls, year)
    frame = Frame(data, collect.columns)
    
    return frame.get_json_data()

@app.get('/importacao/{year}')
async def get_importacao(
    year: Annotated[int, Path(title="The ID of the item to get", ge=1970, le=2022)], 
    subtype: ImportacaoModel
):
    urls = collect.get_complex_url(year, 'importacao', subtype)
    data = collect.get_data(urls, year)
    frame = Frame(data, collect.columns)
    
    return frame.get_json_data()

@app.get('/exportacao/{year}')
async def get_exportacao(
    year: Annotated[int, Path(title="The ID of the item to get", ge=1970, le=2022)], 
    subtype: ExportacaoModel
):
    urls = collect.get_complex_url(year, 'exportacao', subtype)
    data = collect.get_data(urls, year)
    frame = Frame(data, collect.columns)
    
    return frame.get_json_data()

# Get full data

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
