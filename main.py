from utils.structure.data_functions import get_data

if __name__ == '__main__':
    data = get_data()
    print(type(data))
    print( data.to_json() )
    print('Collect Finished')



'''
Pontos para se trabalhar com a API

    1. Hoje coleto o data através de uma lista completa(com todos os anos) que retorna um dataframe bruto, o retorno de uma das APIs até pode ser o conteúdo de todos os anos, mas eu devo adaptar o conteúdo para que ele retorne um dict tratado (sem as linhas nulas e sem '-' e '*');
        1.1 Considerando isso, tenho que fazer alguma adaptação para quando a chamada realizar 


;'''