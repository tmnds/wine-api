import requests
from bs4 import BeautifulSoup
from utils.config import url_abas
# from utils.structure.df_creator import Structure
from utils.structure.data_collector import Collector

url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?'
year_list = [f'ano={x}' for x in range(1970, 2023)]

'''
 Class responsável pela solicitação HTTP na página, e tratamento dos dados.

    - Pensar se poderá ser dividida em duas classes para realização do tratamento dos dados.
'''

# collect = Collector()

def get_request(url):
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
        
            return soup.thead.parent
        else: 
            print('Fail Connection')
            
    except Exception as e:
        print(f'Fail Connection: Error - {e}')

def producao(url, url_abas, year_list):
    # retorna uma lista das urls a serem consultadas do topico de producao
    return [ url+ year_list[x] + url_abas['producao'] for x in range(len(year_list))]

def processamento(url, url_abas, year_list):
    # retorna uma lista das urls a serem consultadas do topico de processamento

    viniferas = [ 
        url + 
        year_list[x] + 
        url_abas['processamento']['aba'] + 
        url_abas['processamento']['viniferas']  
        for x in range(len(year_list))
    ]

    americanas_hibridas = [ 
        url + 
        year_list[x] + 
        url_abas['processamento']['aba'] + 
        url_abas['processamento']['americanas_hibridas']  
        for x in range(len(year_list))
    ]

    return viniferas, americanas_hibridas

def get_data():
    '''
    Função responável pela chamada das funções que contêm as urls e respectivos anos do Website.
        Ex: Produção, Processamento ...
    
    Questões:

    1. Quando eu fizer o loop, será um loop de todos os anos, considerando isto, haverá várias colunas repetidas, talvez, limitar de acordo com a aba que está sendo processada.
        - Ou dividir em uma função especifica para cada aba a ser processada.
    '''
    urls = producao(url, url_abas, year_list)
    
    for i in range(len(urls)): # Esse loop pode só funcionar para produção, para os demais pode dar problema
        filter = get_request(urls[i])

        columns_dataset = [filter.find_all('th')[i].string.strip() for i in range(len(filter.find_all('th')))]
        print(columns_dataset)

        dataset = [filter.find_all('td')[i].string.strip() for i in range(len(filter.find_all('td')))]
        print(dataset)

    # url_1, url_2 = processamento(url, url_abas, year_list)

    # for i in range(len(url_1)):
        # get_request(url_1[i])
        # get_request(url_2[i])

if __name__ == '__main__':
    get_data()
    print('Collect Finished')

    # print(collect.columns)

    # print(url_abas['processamento']['aba'])
    # print(url_abas['processamento']['sem_classificacao'])
