import requests
from bs4 import BeautifulSoup

erro = "Erro ao acessar a página da Embrapa)"
soup = ""

def get_producao_data():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02"
    response = requests.get(url)
    valida_URL (response, soup)
    
    # Lógica de extração de dados
    data = {"example_key": "example_value"}  # substitua por dados reais extraídos
    return data

def get_processamento_data():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03"
    response = requests.get(url)
    valida_URL (response, soup)
    
    # Lógica de extração de dados
    data = {"example_key": "example_value"}  # substitua por dados reais extraídos
    return data

def get_comercializacao_data():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04"
    response = requests.get(url)
    valida_URL (response, soup)

    # Lógica de extração de dados
    data = {"example_key": "example_value"}  # substitua por dados reais extraídos
    return data

def get_importacao_data():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05"
    response = requests.get(url)
    valida_URL (response, soup) 

    # Lógica de extração de dados
    data = {"example_key": "example_value"}  # substitua por dados reais extraídos
    return data

def get_exportacao_data():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06"
    response = requests.get(url)
    valida_URL (response, soup)  
    # Lógica de extração de dados
    data = {"example_key": "example_value"}  # substitua por dados reais extraídos
    return data
 
def valida_URL(response, soup):
    # Verificando se conseguimos extrair os dados da URL
    if response.status_code == 200:
      soup = BeautifulSoup(response.content, "html.parser")
    else:
      return erro
