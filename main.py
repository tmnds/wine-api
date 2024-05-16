from backend.structure.df_creator import Frame
from backend.structure.data_collector import Collector

'''
Pontos para se trabalhar com a API

    1. Hoje coleto o data através de uma lista completa(com todos os anos) 
        que retorna um dataframe bruto, o retorno de uma das APIs até pode 
        ser o conteúdo de todos os anos, mas eu devo adaptar o conteúdo para 
        que ele retorne um dict tratado (sem as linhas nulas e sem '-' e '*');
        1.1 Considerando isso, tenho que fazer alguma adaptação para quando a 
        chamada realizar 

primeir chama funcao que retorna as urls
url = get_producao()

2. essa funcao vai receber as urls que precisam ser processadas
    get_full_data()
'''



if __name__ == '__main__':
    # req = Requisition()
    collect = Collector()
    urls = collect.get_producao()
    data = collect.get_full_data(urls)
    frame = Frame(data, collect.columns)
    
    print(frame.get_json_data())

