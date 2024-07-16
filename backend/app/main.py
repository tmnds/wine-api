from fastapi import FastAPI, Path, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
 

from backend.structure.df_creator import Frame
from backend.structure.data_collector import Collector
from backend.structure.base_model import ProcessamentoModel, ImportacaoModel, ExportacaoModel, User, UserInDB


app = FastAPI()
collect = Collector()


'''
    Authentication TEST
'''

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

def fake_hash_password(password: str):
    return 'fakehash ed' + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    return get_user(fake_users_db, token)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid authentication credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    return user

async def get_current_activate_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail='Inactive User')
    return current_user

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get('/users/me')
async def read_users_me(current_user: Annotated[User, Depends(get_current_activate_user)]):
    return current_user


'''
Get Year data
'''

@app.get('/')
def route_default():
    return 'Welcome to API Embrapa'

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
