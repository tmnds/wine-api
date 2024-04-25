import requests
from bs4 import BeautifulSoup
from utils.config import url_abas
# from utils.structure.df_creator import Structure
from utils.structure.data_collector import Collector


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

collect = Collector()

def get_request(url):
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'html.parser')
            filter = soup.thead.parent
            
            # columns.append(filter.find_all('th').string.strip())
            # print(columns)
            # print(lenght_columns)

            # print(type(filter.find_all('th')))
            # for x in filter.find_all('th'):
                # print(x)

            # columns = []

            if not 'columns_dataset' in globals():
                columns_dataset = []

            if len(columns_dataset) != len(filter.find_all('th')):
                columns_dataset = [filter.find_all('th')[i].string.strip() for i in range(len(filter.find_all('th')))]
                print('#DEBUG')


            print(columns_dataset)
            # if lenght_columns != 0:
                # for i in range(len(filter.find_all('th'))):
                    # print(filter.find_all('th')[i].string.strip()) 
                    # collect.add_column(filter.find_all('th')[i].string.strip())
            
                # lenght_columns -= 1 

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

def get_data_loop():
    # funcao responsavel para chamada das demais funcoes

    '''
    criar logica para identificar quantas colunas tem cada seção

    PROBLEMA DE ESTRUTURA
    quando eu fizer o loop, será um loop de todos os anos, considerando isto, haverá várias colunas repetidas.
    pensar no tratamento para isto. talvez, limitar de acordo com a aba que está sendo processada.
    resolver esse problema, considerando que o loop acontecerá várias vezees e os valores internos serão resetados, talvez colocá-los por fora
    '''
    
    urls = producao(url, url_abas, year_list)
    # url_1, url_2 = processamento(url, url_abas, year_list)
    
    for i in range(len(urls)):
        get_request(urls[i])

        # logica para armazenar os dados no dataframe?
            # for i in range(len(filter.find_all('td'))):
                # print(filter.find_all('td')[i].string.strip())
                # collect.add_data(filter.find_all('td')[i].string.strip())


    # url_1, url_2 = processamento(url, url_abas, year_list)
    # print(url_1, url_2)
    # for i in range(len(url_1)):
        # get_request(url_1[i])
        # get_request(url_2[i])

    # 1. inserir os dados um a um?
    # 2. manter os dados em uma lista e depois inseri-los?

if __name__ == '__main__':
    # print(producao(url, url_abas, year_list))
    # get_request(url)
    get_data_loop()
    print('Collect Finished')

    # print(collect.columns)

    # print(url_abas['processamento']['aba'])
    # print(url_abas['processamento']['sem_classificacao'])
