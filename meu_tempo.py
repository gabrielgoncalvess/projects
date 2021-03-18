# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:49:13 2021

@author: gabre
"""

import requests
import json 
import datetime

token = "728e73adaf650e3bc63d786a377135f4"


estado = "RJ"#input("Digite o estado: ")
city = "Rio de Janeiro"#input("Digite a cidade: ")


url = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=" + str(city) + "&state=" + estado + "&token=" + str(token)

#response1 = requests.get(url)

response = requests.request("GET", url)

#retorno = json.loads(response.content)

retorno = json.loads(response.text)


id_cidade = retorno[0]['id']

tempo = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/" + str(id_cidade) + "/hours/72?token=" + str(token)


response2 = requests.request("GET", tempo)

retorno2 = json.loads(response2.text)

#'http://apiadvisor.climatempo.com.br/api-manager/user-token/:your-app-token/locales' \
         #-H 'Content-Type: application/x-www-form-urlencoded' \
         #-d 'localeId[]=3477'

# Cadastrar cidade (só pode mudar depois de 24h)
'''
url3 = 'http://apiadvisor.climatempo.com.br/api-manager/user-token/' + str(token) + '/locales'
payload = "localeId[]=" + str(id_cidade)
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response3 = requests.request("PUT", url3, headers = headers, data = payload)
retorno3 = json.loads(response3.text)
'''

'''
# Ver quais estão disponíveis
url2 = 'http://apiadvisor.climatempo.com.br/api-manager/user-token/' + str(token) + '/locales'

response3 = requests.request("GET", url2)

#retorno = json.loads(response.content)

retorno3 = json.loads(response3.text)
'''

url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/" + str(id_cidade) + "/current?token=" + str(token)

#response1 = requests.get(url)

response = requests.request("GET", url)

#retorno = json.loads(response.content)

retorno = json.loads(response.text)

cidade = retorno['name']
estado = retorno['state']

temperatura = retorno['data']['temperature']
condicao = retorno['data']['condition']
sensacao_termica = retorno['data']['sensation']
data_hora = retorno['data']['date']
data_conver = datetime.datetime.strptime(data_hora, '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')

print(f"Estado: {estado}  Cidade: {cidade}")
print(f"Temperatura: {temperatura}")
print(f"Condição: {condicao}")
print(f"Sensação Térmica: {sensacao_termica}")
print(f"Data e hora: {data_conver}")
