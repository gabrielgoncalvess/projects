# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:51:19 2021

@author: gabre
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd

my_url = "https://www.amazon.com.br/gp/bestsellers/books/?ie=UTF8&ref_=sv_b_2"

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html,"html.parser")

# grabs each product
containers = page_soup.findAll("div",{"class":"a-section a-spacing-none aok-relative"})
#container = containers[0]



lista1=[]
lista2=[]
lista3=[]
lista4=[]
lista5=[]

for container in containers:

    nome_livro = container.a.img["alt"]
    
    div_autor = container.findAll("div",{"class":"a-row a-size-small"})
    autor = div_autor[0].text
    
    div_rating = container.findAll("div",{"class":"a-icon-row a-spacing-none"})
    if div_rating != []:
        rating = div_rating[0].i.text
        div_aval = div_rating[0].findAll("a",{"class":"a-size-small a-link-normal"})
        num_aval = div_aval[0].text
    else:
        rating = ""
        num_aval = ""
    div_preco = container.findAll("div",{"class":"a-row"})
    preco = div_preco[3].span.span.text
    
    lista1.append(nome_livro)
    lista2.append(rating)
    lista3.append(num_aval)
    lista4.append(autor)
    lista5.append(preco)
    
    #print(nome_livro)
    #print(autor)
    #print(rating)
    #print(num_aval)

df = pd.DataFrame({'Nome do Livro':lista1,'Autor':lista4,'Rating':lista2,'Num Aval':lista3,'Preço':lista5})
df.to_excel('livros_v2.xlsx')



    
    