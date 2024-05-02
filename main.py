'''
Script de chamada
'''
import timeit

from utils.requests.request import *
from utils.structure.df_creator import schema


def get_data():
    '''
    Função responável pela chamada das funções que contêm as urls e respectivos anos do Website.
        Ex: Produção, Processamento ...
    
    Etapa 1
        -> Ao definir as colunas, deverá ser inserido a nova coluna ao final 'Ano'
    Etapa 2
        -> Em cada loop de Ano, os dataframes devem possuir a informação de cada Loop, no seguinte formato:
        Ano 1970
        [['VINHO DE MESA', '217.208.604', '1970'], ['coluna1', 'coluna2', 'coluna3'], ['coluna1', 'coluna2', 'coluna3'], ['coluna1', 'coluna2', '1970'] ...]
        Ano 1971
        [['VINHO DE MESA', '217.208.604', '1971'], ['coluna1', 'coluna2', 'coluna3'], ['coluna1', 'coluna2', 'coluna3'], ['coluna1', 'coluna2', '1971'] ...]

    '''
    urls = producao(url, url_abas, year_list)
    
    for i in range(len(urls)): # Esse loop pode só funcionar para produção, para os demais pode dar problema
        filter = get_request(urls[i])
        # print(year_list[i])
        print(filter)

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

    # get_dat = timeit.timeit("get_data()", globals=globals(),number=1)
    get_data()
    # print(f'tempo: {get_data}') # 150.86416650001775
    # print(collect.columns)
    # print(collect.data)

    print('Collect Finished')



