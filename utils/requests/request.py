import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
r = requests.get('http://vitibrasil.cnpuv.embrapa.br/', headers=headers)




print(r.status_code)

