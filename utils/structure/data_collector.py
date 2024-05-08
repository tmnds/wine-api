class Collector:

    '''
    Classe responsável pela coleta dos dados

    Realizará o armazenamento em memória. Pensar na utilização de Threads e paralelismo.
    '''

    def __init__(self):
        self.columns = None
        self.data = []

    def add_column(self, column):
        self.columns = column

    def add_data(self, data):
        self.data.append(data)
    
    def adjust_data(self):
        new_data = []
        [new_data.extend(element) for element in self.data]
        return new_data
    
    def clear_list(self):
        self.data.clear()
    
    