from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
 
lista_cidades = []
url = 'https://bancosbrasil.com.br/agencias/banco-do-brasil-sa/rio-grande-do-sul/1'
cidades_xpath = '//div[@id="pesquisa"]/a'
 
driver = webdriver.Chrome()
driver.get(url)
sleep(2)
 
elementos_links = driver.find_elements(By.XPATH, cidades_xpath)
 
for elemento_link in elementos_links:
    link_cidade = elemento_link.get_attribute('href')
    lista_cidades.append(link_cidade)
 
lista_cidades_sem_duplicatas = list(set(lista_cidades))
lista_link_botoes = []
lista_dados_agencia = []  
lista_endereco_agencia = []  
 
for link in lista_cidades_sem_duplicatas:
    url_cidade = link
    driver.get(url_cidade)
    sleep(1)
    buttons_elements = driver.find_elements(By.XPATH, '//tbody[@id="getBancosTable"]//a')
 
    for element in buttons_elements:
        link_agencia = element.get_attribute('href')
        
        lista_link_botoes.append(link_agencia)
 
for unidade in lista_link_botoes:
    driver.get(unidade)
    sleep(1)
    agencia_dados = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[1]/div/div[1]').text
    
    agencia_endereco = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[1]/div/div[2]').text
    
    
    lista_dados_agencia.append(agencia_dados)
    lista_endereco_agencia.append(agencia_endereco)
 

df = pd.DataFrame({
    'Dados Agencia': lista_dados_agencia,
    'Endereço Agencia': lista_endereco_agencia
})
 

df.to_excel('agencias-bb_RS.xlsx', index=False)
 
driver.quit()