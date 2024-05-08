import pandas as pd
import numpy as np



class Frame:
    
    def __init__(self, data, columns):
        self.df = pd.DataFrame(data=data, columns=columns)
    
    '''
    Armazenar dados das colunas que já sao listas em outras listas? Nao faz muito sentido
    '''
    
    def print_frame(self):
        print(self.df)
