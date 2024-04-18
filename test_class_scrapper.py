import requests


class Scrapper:

    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
   #r = requests.get('http://vitibrasil.cnpuv.embrapa.br/', headers=headers)

    def __init__(self):
        self.producao = '/index.php?opcao=opt_02'
        self.url = 'http://vitibrasil.cnpuv.embrapa.br/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    def check_status(self.):
        return
    if r.status_code == 200:
        print(r.headers)
        print(r.url) 
    else:
        print('fail')


    def get_producao():

    #passar os params
    #http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02
