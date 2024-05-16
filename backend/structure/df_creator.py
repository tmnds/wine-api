import pandas as pd


class Frame:
    '''
    Armazenar dados das colunas que já sao listas em outras listas? Nao faz muito sentido
    '''
    def __init__(self, data, columns):
        self.df = pd.DataFrame(data=data, columns=columns)
    
    def print_frame(self):
        print(self.df)
    
    def replace_data(self):
        return self.df.replace({'-': None}).replace({'*': None})

    def get_json_data(self):
        modified_data = self.replace_data()
        return modified_data.to_dict('records')

    

