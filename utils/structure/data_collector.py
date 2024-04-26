class Collector:

    '''
    Classe responsável pela coleta dos dados

    Realizará o armazenamento em memória. Pensar na utilização de Threads e paralelismo.
    '''

    def __init__(self):
        self.columns = []
        self.data = []

    def add_column(self, column):
        self.columns.append(column)

    def add_data(self, data):
        self.data.append(data)
    
    