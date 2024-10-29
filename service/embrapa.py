import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError, Timeout
import time

error_message = "Error accessing the Embrapa page"
soup = ""

def get_production_data():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02"
    soup = validate_url(url)
    
    if soup:
        # Example of data extraction
        data = extract_data(soup)
        return data
    else:
        return {"error": error_message}

def get_processing_data():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03"
    soup = validate_url(url)
    
    if soup:
        data = extract_data(soup)
        return data
    else:
        return {"error": error_message}

def get_commercialization_data():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04"
    soup = validate_url(url)

    if soup:
        data = extract_data(soup)
        return data
    else:
        return {"error": error_message}

def get_import_data():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05"
    soup = validate_url(url)

    if soup:
        data = extract_data(soup)
        return data
    else:
        return {"error": error_message}

def get_export_data():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06"
    soup = validate_url(url)

    if soup:
        data = extract_data(soup)
        return data
    else:
        return {"error": error_message}

def extract_data(soup):
    # Locate the table with class "tb_base"
    table = soup.find("table", class_="tb_base tb_dados")
    data = {}

    if table:
        # Extract table headers
        headers = [header.get_text(strip=True) for header in table.find_all("th")]
        rows = []
        
        # Extract rows and cells
        for row in table.find_all("tr")[1:]:  # Skip the header
            cells = [cell.get_text(strip=True) for cell in row.find_all("td")]
            rows.append(dict(zip(headers, cells)))
        
        data["table_data"] = rows
    else:
        data["message"] = "No data found in the specified format."
    
    return data

def validate_url(url, max_retries=3, delay=2):
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url, timeout=5)  # Timeout to avoid indefinite waiting
            if response.status_code == 200:
                return BeautifulSoup(response.content, "html.parser")
            else:
                print(f"Error accessing URL: {url} - Status code: {response.status_code}")
                return None
        except (ConnectionError, Timeout) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            attempt += 1
            time.sleep(delay)  # Wait before retrying
    print(error_message)
    return None
