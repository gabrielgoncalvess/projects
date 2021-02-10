# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:51:19 2021

@author: gabre
"""

# Top 50 books - Amazon

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



list1=[]
list2=[]
list3=[]
list4=[]
list5=[]

for container in containers:

    book_name = container.a.img["alt"]
    
    div_author = container.findAll("div",{"class":"a-row a-size-small"})
    author = div_author[0].text
    
    div_rating = container.findAll("div",{"class":"a-icon-row a-spacing-none"})
    if div_rating != []:
        rating = div_rating[0].i.text
        div_aval = div_rating[0].findAll("a",{"class":"a-size-small a-link-normal"})
        num_aval = div_aval[0].text
    else:
        rating = ""
        n_aval = ""
    div_price = container.findAll("div",{"class":"a-row"})
    price = div_price[3].span.span.text
    
    lista1.append(book_name)
    lista2.append(rating)
    lista3.append(n_aval)
    lista4.append(author)
    lista5.append(price)

df = pd.DataFrame({'Title':list1,'Author':list4,'Rating':list2,'Num Aval':list3,'Price':list5})
df.to_excel('books_v2.xlsx')



    
    
