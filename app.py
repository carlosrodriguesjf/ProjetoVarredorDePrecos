# PROJETO AUTOMAÇÃO WEB - VARREDOR DE PREEÇOS

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime as dt
import schedule
import os


def main():
    def iniciar_driver():
        chrome_options = Options()
        arguments = ['--lang=en-US', '--window-size=1920,1080',
                 '--incognito', '--disable-gpu', '--no-sandbox', '--headless', '--disable-dev-shm-usage' ]
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

    produtos = ['Console Playstation 5', 'cadeira gamer', 'hd ssd 1tb']

    data = dt.date.today().strftime("%d_%b")
    hora = dt.datetime.now().strftime('%H_%M')

    nome_pasta = str(data)+"_"+str(hora)

    os.mkdir(nome_pasta)

    for produto in produtos:
        # Acessando o site www.zoom.com.br
        driver.get('https://www.zoom.com.br')

        # Acessando o produto Console Playstation 5 
        campo_busca = driver.find_element(By.XPATH,'//div/input[@placeholder="Digite sua busca..."]')
        sleep(1)
        campo_busca.click()
        sleep(1)
        campo_busca.send_keys(produto)
        sleep(1)
        campo_busca.send_keys(Keys.ENTER)
        sleep(1)

        # Selecionando o nome, preço e link de compra dos Consoles Playstation 5
        sleep(2)
        nomes = driver.find_elements(By.XPATH, "//div//div[@class='ProductCard_ProductCard_NameWrapper__lOyZM']//h2")
        precos = driver.find_elements(By.XPATH,"//div//p[@data-testid='product-card::price']")
        links = driver.find_elements(By.XPATH,"//div/a[@class='ProductCard_ProductCard_Inner__tsD4M']")

        nome_arquivo = produto.lower().replace(' ','_')+'_'+str(data)+'.csv'

        caminho_arquivo = os.path.join(nome_pasta,nome_arquivo)

        for nome,preco,link in zip(nomes,precos,links):
            # Extraindo o link de compra
            link_processado = link.get_attribute('href')
        
            # Criando arquivo relativo a Console Playstation 5
            with open(caminho_arquivo,'a',encoding='utf-8', newline='') as arquivo:
                arquivo.write(f'{nome.text};{preco.text};{link_processado}'+os.linesep) 

    driver.quit()
    print('Fim da Execução')
main()


# Agendando a execução do programa para todo dia 0:00 h
schedule.every().day.at('15:25').do(main)

while True:
    schedule.run_pending()
    sleep(1)


