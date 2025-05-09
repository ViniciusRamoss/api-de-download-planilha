from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurações para ignorar erros SSL
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_experimental_option("detach", True)  # Mantém o navegador aberto

# Inicializa o navegador com as opções configuradas
navegador = webdriver.Chrome(options=chrome_options)
navegador.get('https://ri.magazineluiza.com.br/#')

# Localiza o elemento usando By.XPATH e clica nele
navegador.find_element(By.XPATH, '//*[@id="splash"]/div[1]/a').click()
navegador.find_element(By.XPATH, '//*[@id="Form1"]/header/div/div/div/div[2]/ul/li[3]/a').click()

# Aguarde até que o elemento esteja visível e clicável
wait = WebDriverWait(navegador, 10)  # Tempo máximo de espera: 10 segundos

# Localiza e clica no elemento
elemento = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Form1"]/div[10]/div/div/div/div/ul[3]/li[2]/a')))
elemento.click()
navegador.find_element(By.XPATH, '//*[@id="QkuLGwWq7MtNAgC4qqZQKg=="]').click()

# Aguarde o usuário pressionar Enter antes de fechar o navegador
input("Pressione Enter para fechar o navegador...")