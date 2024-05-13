import pandas as pd


class Frame:
    '''
    Armazenar dados das colunas que já sao listas em outras listas? Nao faz muito sentido
    '''
    def __init__(self, data, columns):
        self.df = pd.DataFrame(data=data, columns=columns)
    
    def print_frame(self):
        print(self.df)