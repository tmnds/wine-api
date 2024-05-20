from backend.requests.http_request import Requisition


class Collector(Requisition):
    '''
    Classe responsável pela coleta dos dados
    Realizará o armazenamento em memória. Pensar na utilização de Threads e paralelismo.
    '''

    def __init__(self):
        super().__init__()
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
    
    def get_data(self, urls, year):
    
        filter = super().get_request(urls)

        if self.columns is None:
            self.add_column(
                [filter.find_all('th')[i].string.strip() for i in range(len(filter.find_all('th')))]
            )
            self.columns.append('Ano')

        self.add_data(
            [
                [
                    _.find_all('td')[0].get_text(strip=True), 
                    _.find_all('td')[1].get_text(strip=True), 
                    year
                ] 
                for _ in filter.find_all('tr') 
                    if len(_.find_all('td')) == 2
            ]
        )
        return self.adjust_data()

    def get_full_data(self, urls):
    
        for i in range(len(urls)): 
            filter = super().get_request(urls[i])

            if self.columns is None:
                self.add_column(
                    [filter.find_all('th')[i].string.strip() for i in range(len(filter.find_all('th')))]
                )
                self.columns.append('Ano')

            if len(self.columns) == 3:
                self.add_data(
                    [
                        [
                            _.find_all('td')[0].get_text(strip=True), 
                            _.find_all('td')[1].get_text(strip=True), 
                            Requisition.year_list[i]
                        ] 
                        for _ in filter.find_all('tr') 
                            if len(_.find_all('td')) == 2
                    ]
                )
            else:
                self.add_data(
                [
                    [
                        _.find_all('td')[0].get_text(strip=True), 
                        _.find_all('td')[1].get_text(strip=True), 
                        _.find_all('td')[2].get_text(strip=True),
                        Requisition.year_list[i]
                    ] 
                    for _ in filter.find_all('tr') 
                        if len(_.find_all('td')) == 3
                ]
            )

        return self.adjust_data()
