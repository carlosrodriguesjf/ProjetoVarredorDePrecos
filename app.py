# PROJETO AUTOMAÇÃO WEB - VARREDOR DE PREEÇOS

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

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
driver.get('https://www.zoom.com.br')

# Acessando o produto Console Playstation 5 
campo_busca = driver.find_element(By.XPATH,'//div/input[@placeholder="Digite sua busca..."]')
sleep(1)
campo_busca.click()
sleep(1)
campo_busca.send_keys('Console Playstation 5')
sleep(1)
campo_busca.send_keys(Keys.ENTER)



# Selecionar o nome e preço dos 3 primeiro produtos e salvar em uma lista


# Digitar Cadeira Gamer no campo busca 

# Selecionar o nome e preço dos 3 primeiro produtos e salvar em uma lista


# Digitar SSD de 1TB no campo busca 

# Selecionar o nome e preço dos 3 primeiro produtos e salvar em uma lista



driver.quit()


# Salvar todos os dados em uma planilha


# Agendar a execução do programa para todo dia 0:00 h




# Fazer o deploy em uma VPS


