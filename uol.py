# Wagner Carlos Mariani
# 16-10-2023
# Exemplo de uso do Selenium para acessar o site do UOL e aceitar os cookies.
# mineracao de dados - UTFPR - 2023


from selenium import webdriver  # Importa o módulo principal do Selenium para interagir com navegadores web.
from selenium.webdriver.common.by import By  # Importa os métodos para selecionar elementos com base em diferentes propriedades.
from selenium.webdriver.support.ui import WebDriverWait  # Permite esperar por um certo estado ou condição.
from selenium.webdriver.support import expected_conditions as EC  # Coleção de condições predefinidas que podem ser usadas com o WebDriverWait.



# O caminho para o geckodriver. driver pro Firefox
#driver_path = r'C:\Users\wagne\selenium\src\geckodriver.exe'
driver_path = r'.\geckodriver.exe'


# Define o serviço
service = webdriver.firefox.service.Service(driver_path)

# Inicializa o navegador Firefox com o serviço definido
browser = webdriver.Firefox(service=service)

browser.get('https://www.uol.com.br')

# Aguarda um pouco para a página carregar completamente
browser.implicitly_wait(10)  # 10 segundos (espera implícita)

# Rola até o final da página
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# Clica no botão para aceitar os cokies.
wait = WebDriverWait(browser, 10) # 10 segundos (espera explícita)
ok_button = browser.find_element(By.CLASS_NAME, "banner-lgpd-consent__accept") # localizando por nome da classe
browser.execute_script("arguments[0].click();", ok_button)  # qui usamos JavaScript para "forçar" um clique no botão.


