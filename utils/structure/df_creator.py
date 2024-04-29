import pandas as pd
import numpy as np


'''
Armazenar dados das colunas que já sao listas em outras listas? Nao faz muito sentido
'''
def schema(data, columns):
    df = pd.DataFrame(data=data, columns=columns)
    print(df)

if __name__ == '__main__':

    struct = Structure(data)
    struct.columns.append(column1)
    struct.columns.append(column2)

    print(struct.columns)
