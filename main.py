'''
Script de chamada
'''
import timeit

from utils.requests.http_request import Requisition
from utils.structure.df_creator import Frame
from utils.structure.data_collector import Collector
from utils.config import url_abas

collect = Collector()
req = Requisition(url_abas)

def get_data():
    '''
    Função responável pela chamada das funções que contêm as urls e respectivos anos do Website.
        Ex: Produção, Processamento ...
    '''
    # urls = req.get_producao()
    # urls = req.get_comercializacao()
    # urls = req.get_processamento()
    # urls = req.get_importacao()
    urls = req.get_exportacao()

    if isinstance(urls, dict):
        print('Dict #DEBUG')
        get_data_dict(urls)

    if isinstance(urls, list):
        print('Lists #DEBUG')
        get_data_list(urls)
        

def get_data_list(urls):
    
    for i in range(len(urls)): 
        filter = req.get_request(urls[i])

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
                    req.year_list[i][4:]
                ] 
                for _ in filter.find_all('tr') 
                    if len(_.find_all('td')) == 2
            ]
        )
        
    frame = Frame(collect.adjust_data(), collect.columns)
    frame.print_frame()
    
def get_data_dict(urls):

    for key, value in urls.items():
        key_json = key
        values_json = value.keys()

    for types in values_json:
        print(types)
        
        for i in range(len(urls[key_json][types])):
            # print(urls[key_json][types][i])
            filter = req.get_request(urls[key_json][types][i])

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
                        _.find_all('td')[2].get_text(strip=True),
                        req.year_list[i][4:]
                    ] 
                    if len(_.find_all('td')) > 2
                    else
                    [
                        _.find_all('td')[0].get_text(strip=True) if len(_.find_all('td')) == 2 else None, 
                        _.find_all('td')[1].get_text(strip=True) if len(_.find_all('td')) == 2 else None, 
                        req.year_list[i][4:] if len(_.find_all('td')) == 2 else None
                    ] 
                    for _ in filter.find_all('tr') 
                ]
            )
            
        '''
        Pontos de Ajuste:
            Considerando que o ELSE da lista de comprehension deveria apenas trazer Null para a primeira linha apenas do topico de comercializacao, por ser o unico dict com 3 colunas. 

            1. Por que isso acontece com todos os outros topicos DICT, ex: importacao, exportacao..;
            2. Como resolver os valores Null;
        '''
        frame = Frame(collect.adjust_data(), collect.columns)
        frame.print_frame()
        collect.clear_list()

if __name__ == '__main__':

    # get_dat = timeit.timeit("get_data()", globals=globals(),number=1)
    # print(f'tempo: {get_dat}') # 150.86416650001775

    get_data()
    print('Collect Finished')
    