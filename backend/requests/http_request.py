import requests
from bs4 import BeautifulSoup
from json import load


class Requisition:
    '''
    Class responsável pela solicitação HTTP na página, e tratamento dos dados.
        - Pensar se poderá ser dividida em duas classes para realização do tratamento dos dados.
    '''
    year_list = [i for i in range(1970, 2023)]

    def __init__(self):
        self.url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?'
        self.url_abas = load( open('backend/config.json') )

    def get_request(self, url):
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; i64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        
        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                return soup.thead.parent
            
        except Exception as e:
            return f'Fail Connection: Error - {e}'

    def get_simple_url(self, year, type):
        if year not in self.year_list:
            raise Exception('The year entered does not correspond to the value available annual values')
        
        return self.url + f'ano={str(year)}' + self.url_abas[type]

    def get_full_simple_url(self, type):
        return [ self.url+ f'ano={self.year_list[i]}' + self.url_abas[type] for i in range(len(self.year_list))]

    def get_complex_url(self, year, type, subtype):
        if year not in self.year_list:
            raise Exception('The year entered does not correspond to the value available annual values')
        
        return  self.url + f'ano={year}' + self.url_abas[type]['aba'] + self.url_abas[type][subtype]  
    
    def get_full_complex_url(self, type, subtype):

        return [ 
            self.url + 
            f'ano={self.year_list[i]}' + 
            self.url_abas[type]['aba'] + 
            self.url_abas[type][subtype]  
            for i in range(len(self.year_list))
        ]