import pandas as pd
import numpy as np


'''
classe de dataframe vai receber os valores que foram raspadas da pagina web
atraves dos loops do get_data()
eh importante entender como sera definido os campos titulos dos dataframes, e ainda aqui, teremos uma serie de dataframes diferentes
'''
class Structure:
    def __init__(self, data):
        self.columns = []
        self.data = data
    
    def add_data(self, data):
        self.columns.append(data)
    
    # def get_values(self):


if __name__ == '__main__':

    struct = Structure(data)
    struct.columns.append(column1)
    struct.columns.append(column2)

    print(struct.columns)



'''

column1= 'Quantidade'
column2= 'Valor'
columns = ['Quantidade', 'Valor']
data = {columns[0]: [1, 2, 3], columns[1]: [1.43, 1.39, 1.00]}
df = pd.DataFrame(data=data, columns=columns)


columns = ['column1', 'column2', 'column3']

columns = ['column1', 'column2']


qtt_columns = len(columns) # saber a quantidade de colunas para criar o dataframe

data = {
    columns[0]: [data_array],
    columns[1]: [data_array],
    columns[2]: [data_array]
}

'''
