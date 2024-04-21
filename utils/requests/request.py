import requests
# import json
# import ast
from bs4 import BeautifulSoup
from utils.config import url_abas

url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?'
year_list = [f'ano={x}' for x in range(1970, 2023)]


'''
1. fazer um loop dos anos. 
2. em cada ano, entrar no table class = 'tb_base tb_dados'
3. na thread pegar o <tr> e depois <th> para pegar Produto e Quantidade (L.) - estes estão os headers 
4. entrar no <tbody> depois <tr> e buscar o produto e subproduto, sendo <td class='tb_item'> com dois valores
5. ainda no <tbody> depois <tr> e buscar o produto e subproduto, sendo <td class='tb_subitem'> com dois valores
6. entender que quando o valor de td class='tb_item', então, produto. Se 'tb_subitem', então, subproduto

# http://vitibrasil.cnpuv.embrapa.br/index.php?ano=1999&opcao=opt_03&subopcao=subopt_01
# http://vitibrasil.cnpuv.embrapa.br/index.php?ano=1970&opcao=opt_03&subopcao=subopt_02
'''

def get_request(url):
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            filter = soup.thead.parent
            print('Sucess Connection')
            
            print(filter.find_all('th')[0].string) 
            print(filter.find_all('th')[1].string)
            
            for i in range(len(filter.find_all('td'))):
                print(filter.find_all('td')[i].string.strip())
    
            # return soup.thead.parent
        else: 
            print('Fail Connection')
            
    except Exception as e:
        print(f'Fail Connection: Error - {e}')


def producao(url, url_abas, year_list):
    # retorna uma lista das urls a serem consultadas do topico de producao
    return [ url+ year_list[x] + url_abas['producao'] for x in range(len(year_list))]


def get_data():
    
    urls = producao(url, url_abas, year_list)
    
    for i in range(len(urls)):
        get_request(urls[i])
      
if __name__ == '__main__':
    # print(producao(url, url_abas, year_list))
    # get_request(url)
    get_data()
    

