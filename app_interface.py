import tkinter as tk
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import urllib
import time

def abrir_arquivo():
    file_path = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx")])
    arquivo_entry.delete(0, tk.END)
    arquivo_entry.insert(0, file_path)

def validacao_numero(navegador, numero):
        # verifica de o número é valido
    if len(navegador.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:

        # envia mensagem
        navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
        time.sleep(2)

def enviar_mensagens():
    arquivo = arquivo_entry.get()

    if not arquivo:
        resultado_label.config(text="Selecione um arquivo!")
        return

    # Código do Selenium
    navegador = webdriver.Chrome()
    navegador.get('https://web.whatsapp.com')
    
    while len(navegador.find_elements(By.ID, 'side')) < 1:
        time.sleep(1)
    time.sleep(2)
    
    tabela = pd.read_excel(arquivo)
    
    for linha in tabela.index:
        nome = tabela.loc[linha, "nome"]
        numero = tabela.loc[linha, "numero"]
        mensagem = tabela.loc[linha, "mensagem"]
    
        texto = mensagem.replace("NOME", nome)
        texto = urllib.parse.quote(texto)
    
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    
        navegador.get(link)
    
        while len(navegador.find_elements(By.ID, 'side')) < 1:
            time.sleep(1)
        time.sleep(2)

        validacao_numero(navegador, numero)
    
    navegador.quit()
    resultado_label.config(text="Mensagens enviadas com sucesso!")

# Criar a janela
janela = tk.Tk()
janela.title("Envio de Mensagens WhatsApp")

# Criar widgets
arquivo_label = tk.Label(janela, text="Selecione o arquivo Excel:")
arquivo_entry = tk.Entry(janela)
selecionar_button = tk.Button(janela, text="Selecionar Arquivo", command=abrir_arquivo)
enviar_button = tk.Button(janela, text="Enviar Mensagens", command=enviar_mensagens)
resultado_label = tk.Label(janela, text="")

# Posicionar widgets na janela
arquivo_label.pack()
arquivo_entry.pack()
selecionar_button.pack()
enviar_button.pack()
resultado_label.pack()

# Iniciar loop de eventos
janela.mainloop()
