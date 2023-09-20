# PROJETO AUTOMAÇÃO WEB - VARREDOR DE PREEÇOS

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--start-maximized', '--incognito' ]
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()

# Acessando o site www.zoom.com.br
driver.get('https://www.zoom.com.br/search?q=console%20ps5')

# # Acessando o produto Console Playstation 5 
# campo_busca = driver.find_element(By.XPATH,'//div/input[@placeholder="Digite sua busca..."]')
# sleep(1)
# campo_busca.click()
# sleep(1)
# campo_busca.send_keys('Console Playstation 5')
# sleep(1)
# campo_busca.send_keys(Keys.ENTER)
# sleep(1)


# Selecionando o nome, preço e link de compra dos Consoles Playstation 5
sleep(2)
nomes = driver.find_elements(By.XPATH, "//div//div[@class='ProductCard_ProductCard_NameWrapper__lOyZM']//h2")
precos = driver.find_elements(By.XPATH,"//div//p[@data-testid='product-card::price']")
links = driver.find_elements(By.XPATH,"//div/a[@class='ProductCard_ProductCard_Inner__tsD4M']")

# iniciando contador
i=0
data = '04021982'
nome_arquivo = 'precos_ps5_'+data+'.csv'
for nome,preco,link in zip(nomes,precos,links):
    i+=1
    # Extraindo o link de compra
    link_processado = link.get_attribute('href')

    # Criando arquivo relativo a Console Playstation 5
    with open(nome_arquivo,'a',encoding='utf-8', newline='') as arquivo:
        arquivo.write(f' {i} - {nome.text};{preco.text};{link_processado}'+os.linesep) 


# Selecionando o nome, preço e link de compra de cadeira gamer


# Selecionando o nome, preço e link de compra de SSD de 1TB





driver.quit()


# Salvar todos os dados em uma planilha



# Agendar a execução do programa para todo dia 0:00 h




# Fazer o deploy em uma VPS


