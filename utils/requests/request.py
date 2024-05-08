import requests
from bs4 import BeautifulSoup
from utils.config import url_abas

url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?'
year_list = [f'ano={i}' for i in range(1970, 2023)]

'''
 Class responsável pela solicitação HTTP na página, e tratamento dos dados.

    - Pensar se poderá ser dividida em duas classes para realização do tratamento dos dados.
'''

def get_request(url):
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; i64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            return soup.thead.parent
        
    except Exception as e:
        return f'Fail Connection: Error - {e}'

def get_producao(url, url_abas, year_list):
    return [ url+ year_list[i] + url_abas['producao'] for i in range(len(year_list))]

def get_comercializacao(url, url_abas, year_list):
    return [ url+ year_list[i] + url_abas['comercializacao'] for i in range(len(year_list))]

def get_processamento(url, url_abas, year_list):

    viniferas = [ 
        url + 
        year_list[i] + 
        url_abas['processamento']['aba'] + 
        url_abas['processamento']['viniferas']  
        for i in range(len(year_list))
    ]
    
    americanas_hibridas = [ 
        url + 
        year_list[i] + 
        url_abas['processamento']['aba'] + 
        url_abas['processamento']['americanas_hibridas']  
        for i in range(len(year_list))
    ]
    
    uva_mesa = [ 
        url + 
        year_list[i] + 
        url_abas['processamento']['aba'] + 
        url_abas['processamento']['uva_mesa']  
        for i in range(len(year_list))
    ]
    
    sem_classificacao = [ 
        url + 
        year_list[i] + 
        url_abas['processamento']['aba'] + 
        url_abas['processamento']['sem_classificacao']  
        for i in range(len(year_list))
    ]
    
    return {
        'processamento': {
            'viniferas': viniferas,
            'americanas_hibridas': americanas_hibridas,
            'uva_mesa': uva_mesa,
            'sem_classificacao': sem_classificacao
        }
    }


def get_importacao(url, url_abas, year_list):

    vinho_mesa = [ 
        url + 
        year_list[i] + 
        url_abas['importacao']['aba'] + 
        url_abas['importacao']['vinho_mesa']  
        for i in range(len(year_list))
    ]
    
    espumante = [ 
        url + 
        year_list[i] + 
        url_abas['importacao']['aba'] + 
        url_abas['importacao']['espumante']  
        for i in range(len(year_list))
    ]
    
    uva_fresca = [ 
        url + 
        year_list[i] + 
        url_abas['importacao']['aba'] + 
        url_abas['importacao']['uva_fresca']  
        for i in range(len(year_list))
    ]
    
    uva_passa = [ 
        url + 
        year_list[i] + 
        url_abas['importacao']['aba'] + 
        url_abas['importacao']['uva_passa']  
        for i in range(len(year_list))
    ]
    
    suco_uva = [ 
        url + 
        year_list[i] + 
        url_abas['importacao']['aba'] + 
        url_abas['importacao']['suco_uva']  
        for i in range(len(year_list))
    ]
    
    return {
        'importacao': {
            'vinho_mesa': vinho_mesa,
            'espumante': espumante,
            'uva_fresca': uva_fresca,
            'uva_passa': uva_passa,
            'suco_uva': suco_uva
        }
    }

def get_exportacao(url, url_abas, year_list):

    vinho_mesa = [ 
        url + 
        year_list[i] + 
        url_abas['exportacao']['aba'] + 
        url_abas['exportacao']['vinho_mesa']  
        for i in range(len(year_list))
    ]
    
    espumante = [ 
        url + 
        year_list[i] + 
        url_abas['exportacao']['aba'] + 
        url_abas['exportacao']['espumante']  
        for i in range(len(year_list))
    ]
    
    uva_fresca = [ 
        url + 
        year_list[i] + 
        url_abas['exportacao']['aba'] + 
        url_abas['exportacao']['uva_fresca']  
        for i in range(len(year_list))
    ]
    
    suco_uva = [ 
        url + 
        year_list[i] + 
        url_abas['exportacao']['aba'] + 
        url_abas['exportacao']['suco_uva']  
        for i in range(len(year_list))
    ]
    
    return {
        'exportacao': {
            'vinho_mesa': vinho_mesa,
            'espumante': espumante,
            'uva_fresca': uva_fresca,
            'suco_uva': suco_uva
        }
    }
    
if __name__ == '__main__':
    get_processamento(url, url_abas, year_list)
    print()