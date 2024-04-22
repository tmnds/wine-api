import pandas as pd
import numpy as np


# classe de dataframe vai receber os valores que foram raspadas da pagina web
# atraves dos loops do get_data()
# eh importante entender como sera definido os campos titulos dos dataframes, e ainda aqui, teremos uma serie de dataframes diferentes

column1= 'Quantidade'
column2= 'Valor'
columns = ['Quantidade', 'Valor']

data = {columns[0]: [1, 2, 3], columns[1]: [1.43, 1.39, 1.00]}
df = pd.DataFrame(data=data, columns=columns)

print(df)


