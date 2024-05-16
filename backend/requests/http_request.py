import requests
from bs4 import BeautifulSoup
from backend.config import url_abas


class Requisition:
    '''
    Class responsável pela solicitação HTTP na página, e tratamento dos dados.
        - Pensar se poderá ser dividida em duas classes para realização do tratamento dos dados.
    '''
    year_list = [f'ano={i}' for i in range(1970, 2023)]

    def __init__(self):
        self.url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?'
        
        self.url_abas = url_abas

    def get_request(self, url):
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; i64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        
        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                return soup.thead.parent
            
        except Exception as e:
            return f'Fail Connection: Error - {e}'

    def get_producao(self):
        return [ self.url+ self.year_list[i] + self.url_abas['producao'] for i in range(len(self.year_list))]

    def get_comercializacao(self):
        return [ self.url+ self.year_list[i] + self.url_abas['comercializacao'] for i in range(len(self.year_list))]

    def get_processamento_viniferas(self):

        return [ 
            self.url + 
            self.year_list[i] + 
            self.url_abas['processamento']['aba'] + 
            self.url_abas['processamento']['viniferas']  
            for i in range(len(self.year_list))
        ]
    
    def get_processamento_americanas_hibridas(self):
        
        return [ 
            self.url + 
            self.year_list[i] + 
            self.url_abas['processamento']['aba'] + 
            self.url_abas['processamento']['americanas_hibridas']  
            for i in range(len(self.year_list))
        ]

    def get_processamento_uva_mesa(self):

        return [ 
            self.url + 
            self.year_list[i] + 
            self.url_abas['processamento']['aba'] + 
            self.url_abas['processamento']['uva_mesa']  
            for i in range(len(self.year_list))
        ]
    
    def get_processamento_sem_classificacao(self):

        return [ 
            self.url + 
            self.year_list[i] + 
            self.url_abas['processamento']['aba'] + 
            self.url_abas['processamento']['sem_classificacao']  
            for i in range(len(self.year_list))
        ]
        
    def get_importacao_vinho_mesa(self):

        return [ 
            self.url + 
            self.year_list[i] + 
            self.url_abas['importacao']['aba'] + 
            self.url_abas['importacao']['vinho_mesa']  
            for i in range(len(self.year_list))
        ]
    
    def get_importacao_espumante(self):
        
        return [ 
            self.url + 
            self.year_list[i] + 
            self.url_abas['importacao']['aba'] + 
            self.url_abas['importacao']['espumante']  
            for i in range(len(self.year_list))
        ]
    
    def get_importacao_uva_fresca(self):

        return [ 
            self.url + 
            self.year_list[i] + 
            self.url_abas['importacao']['aba'] + 
            self.url_abas['importacao']['uva_fresca']  
            for i in range(len(self.year_list))
        ]
    
    def get_importacao_uva_passa(self):

        return [ 
            self.url + 
            self.year_list[i] + 
            self.url_abas['importacao']['aba'] + 
            self.url_abas['importacao']['uva_passa']  
            for i in range(len(self.year_list))
        ]
    def get_importacao_suco_uva(self):
        
        return [ 
            self.url + 
            self.year_list[i] + 
            self.url_abas['importacao']['aba'] + 
            self.url_abas['importacao']['suco_uva']  
            for i in range(len(self.year_list))
        ]

    def get_exportacao_vinho_mesa(self):

        return [ 
            self.url + 
            self.year_list[i] + 
            self.url_abas['exportacao']['aba'] + 
            self.url_abas['exportacao']['vinho_mesa']  
            for i in range(len(self.year_list))
        ]

    def get_exportacao_espumante(self):

        return [ 
            self.url + 
            self.year_list[i] + 
            self.url_abas['exportacao']['aba'] + 
            self.url_abas['exportacao']['espumante']  
            for i in range(len(self.year_list))
        ]
    def get_exportacao_uva_fresca(self):
        
        return [ 
            self.url + 
            self.year_list[i] + 
            self.url_abas['exportacao']['aba'] + 
            self.url_abas['exportacao']['uva_fresca']  
            for i in range(len(self.year_list))
        ]
    
    def get_exportacao_suco_uva(self):
    
        return [ 
            self.url + 
            self.year_list[i] + 
            self.url_abas['exportacao']['aba'] + 
            self.url_abas['exportacao']['suco_uva']  
            for i in range(len(self.year_list))
        ]
    
if __name__ == '__main__':
    get_processamento(url, url_abas, year_list)
    print()