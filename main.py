'''
Script de chamada
'''
import timeit

from utils.requests.request import *
from utils.structure.df_creator import schema
from utils.structure.data_collector import Collector

collect = Collector()

def get_data():
    '''
    Função responável pela chamada das funções que contêm as urls e respectivos anos do Website.
        Ex: Produção, Processamento ...
    '''
    # urls = producao(url, url_abas, year_list)
    urls = processamento(url, url_abas, year_list)

    if isinstance(urls, dict):
        print('Dict #DEBUG')
        get_data_dict(urls)

    if isinstance(urls, list):
        print('Lists #DEBUG')
        get_data_list(urls)
        

def get_data_list(urls):
    
    for i in range(len(urls)): 
        filter = get_request(urls[i])

        if collect.columns is None:
            collect.add_column(
                [filter.find_all('th')[i].string.strip() for i in range(len(filter.find_all('th')))]
            )
            collect.columns.append('Ano')

        collect.add_data(
            [
                [
                    _.find_all('td')[0].get_text(strip=True), 
                    _.find_all('td')[1].get_text(strip=True), 
                    year_list[i][4:]
                ] 
                 for _ in filter.find_all('tr') 
                    if len(_.find_all('td')) == 2
            ]
        )
    
def get_data_dict(urls):

    for key, value in urls.items():
        key_json = key
        values_json = value.keys()

    for types in values_json:
        print(types)
        
        for i in range(len(urls[key_json][types])):
            # print(urls[key_json][types][i])
            filter = get_request(urls[key_json][types][i])

            if collect.columns is None:
                collect.add_column(
                    [filter.find_all('th')[i].string.strip() for i in range(len(filter.find_all('th')))]
                )
                collect.columns.append('Ano')

            collect.add_data(
                [
                    [
                        _.find_all('td')[0].get_text(strip=True), 
                        _.find_all('td')[1].get_text(strip=True), 
                        year_list[i][4:]
                    ] 
                    for _ in filter.find_all('tr') 
                        if len(_.find_all('td')) == 2
                ]
            )
        
        new_data = collect.adjust_data(collect.data)
        schema(new_data, collect.columns)


if __name__ == '__main__':

    # get_dat = timeit.timeit("get_data()", globals=globals(),number=1)
    # print(f'tempo: {get_dat}') # 150.86416650001775

    get_data()

    # new_data = collect.adjust_data(collect.data)
    # schema(new_data, collect.columns)
    '''
    Ajuste a ser implementado antes de chamar o resto dos processos!!

        - Falta fazer com que o dataframe de cada um dos processos seja criado de forma independente (RESOLVIDO)

        - O Dataframe está appendando os valores;
        - É preciso que os dataframes sejam idenpendentes; 1 daftaframe para cada aba
    '''
    
    # new_data = collect.adjust_data(collect.data)
    # schema(new_data, collect.columns)

    print('Collect Finished')
    