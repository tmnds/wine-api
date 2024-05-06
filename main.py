'''
Script de chamada
'''
import timeit

from utils.requests.request import *
# from utils.structure.df_creator import schema


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
    # urls = producao(url, url_abas, year_list)
    urls = processamento(url, url_abas, year_list)

    if isinstance(urls, dict):
        print('dict')
    
    if isinstance(urls, list):
        print('list')


    # for i in range(len(urls)): 
    #     filter = get_request(urls[i])

    # for i in range(len(urls)): # Esse loop pode só funcionar para produção, para os demais pode dar problema
    #     filter = get_request(urls[i])

    #     if collect.columns is None:
    #         collect.add_column(
    #             [filter.find_all('th')[i].string.strip() for i in range(len(filter.find_all('th')))]
    #         )
    #         collect.columns.append('Ano')

    #     collect.add_data(
    #         [
    #             [
    #                 _.find_all('td')[0].get_text(strip=True), 
    #                 _.find_all('td')[1].get_text(strip=True), 
    #                 year_list[i][4:]
    #             ] 
    #              for _ in filter.find_all('tr') 
    #                 if len(_.find_all('td')) == 2
    #         ]
    #     )

        # collect.add_data(
        #     [
        #         [
        #             _.find_all('td')[0].get_text(strip=True), 
        #             _.find_all('td')[1].get_text(strip=True), 
        #             year_list[i][4:]
        #         ] if len(_.find_all('td')) == 2
        #             else
        #         [
        #             year_list[i][4:]
        #         ]
        #         for _ in filter.find_all('tr')
        #     ]
        # )

        # for _ in filter.find_all('tr'):
        #     if len(_.find_all('td')) == 2:
        #         collect.add_data(
        #             [_.find_all('td')[0].get_text(strip=True), _.find_all('td')[1].get_text(strip=True), year_list[i][4:]]
        #         )


if __name__ == '__main__':

    # get_dat = timeit.timeit("get_data()", globals=globals(),number=1)
    # print(f'tempo: {get_dat}') # 150.86416650001775

    get_data()

    # print(collect.columns)
    # print(collect.data)
    # schema(collect.data, collect.columns)

    print('Collect Finished')



