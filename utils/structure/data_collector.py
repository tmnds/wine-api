class Collector:

    def __init__(self):
        self.columns = []
        self.data = []

    def add_column(self, column):
        self.columns.append(column)

    def add_data(self, data):
        self.data.append(data)
    
    