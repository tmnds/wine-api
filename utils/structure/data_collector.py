


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

    def get_full_data(self, urls):
    
        for i in range(len(urls)): 
            filter = req.get_request(urls[i])

            if self.collect.columns is None:
                self.collect.add_column(
                    [filter.find_all('th')[i].string.strip() for i in range(len(filter.find_all('th')))]
                )
                self.collect.columns.append('Ano')

            self.collect.add_data(
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
        return self.data
