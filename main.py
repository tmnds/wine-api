'''
Script de chamada
...
'''

from utils.requests.request import *
from utils.structure.df_creator import schema


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
        # print(year_list[i])

        if collect.columns is None:
            collect.add_column(
                [filter.find_all('th')[i].string.strip() for i in range(len(filter.find_all('th')))]
            )

        collect.add_data(
            [filter.find_all('td')[i].string.strip() for i in range(len(filter.find_all('td')))]
        )

    # url_1, url_2 = processamento(url, url_abas, year_list)

    # for i in range(len(url_1)):
        # get_request(url_1[i])
        # get_request(url_2[i])


if __name__ == '__main__':
    get_data()
    print(collect.columns)
    print(collect.data)

    schema(collect.data, collect.columns)
    print('Collect Finished')



    '''

    Etapa 1
        -> Ao definir as colunas, deverá ser inserido a nova coluna ao final 'Ano'

    Etapa 2
        -> Em cada loop de Ano, os dataframes devem possuir a informação de cada Loop, no seguinte formato:

        Ano 1970

        [['VINHO DE MESA', '217.208.604', '1970'], ['coluna1', 'coluna2', 'coluna3'], ['coluna1', 'coluna2', 'coluna3'], ['coluna1', 'coluna2', '1970'] ...]

        Ano 1971

        [['VINHO DE MESA', '217.208.604', '1971'], ['coluna1', 'coluna2', 'coluna3'], ['coluna1', 'coluna2', 'coluna3'], ['coluna1', 'coluna2', '1971'] ...]

    '''
