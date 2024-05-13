# wine-api



API responsável pela coleta e disponibilização dos Dados da [Banco de dados de uva, vinho e derivados (embrapa.br)](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01)


Com objetivo de consultar os dados das seguintes abas.

1. Produção
2. Processamento
3. Comercialização
4. Importação
5. Exportação


A API vai servir para alimentar uma base de dados que futuramente será usada para um modelo de Machine Learning.

Objetivos:

1. Criar uma Rest API em Python que faça a consulta no site da Embrapa
    -> Scrapping da Página
2.  A API deve ser documentada.
    -> Utilização de Swagger?
3.  É recomendável (não obrigatório) a escolha de um método de autenticação (JWT, por exemplo)

4. Criar um plano para fazer o deploy da API, desenhando a arquitetura do projeto desde a ingestão até a alimentação do modelo (aqui não é necessário elaborar um modelo de ML, mas é preciso escolher um cenário interessante em que a API possa ser utilizada)
    -> Desde a parte da ingestão do dado, da construção da API e plano de deploy. Plano de Deploy vai depender do ambiente.
5. Fazer um MVP realizando o deploy com um link compartilhável e um repositório no github.
    -> Apenas link do GITHUB