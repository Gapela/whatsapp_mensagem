# import bibliotecas

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import urllib
import time

#Selenium
navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com')

# espera a tela carregar
while len(navegador.find_elements(By.ID, 'side')) < 1:
    time.sleep(1)
time.sleep(2)

# import de dados
tabela = pd.read_excel("msg_wpp.xlsx")

for linha in tabela.index:
    nome = tabela.loc[linha, "nome"]
    numero = tabela.loc[linha, "numero"]
    mensagem = tabela.loc[linha, "mensagem"]

    texto = mensagem.replace("NOME", nome)
    texto = urllib.parse.quote(texto)
    
    # enviar msg
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"

    # abrir o link
    navegador.get(link)

    # espera a tela carregar
    while len(navegador.find_elements(By.ID, 'side')) < 1:
        time.sleep(1)
    time.sleep(2)


    # enviar mensagem
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
    time.sleep(2)
