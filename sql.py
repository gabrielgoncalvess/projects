# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:52:48 2021

@author: gabre
"""

import pandas as pd
import sqlalchemy
import pymysql

# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>

engine = sqlalchemy.create_engine('mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>')

#df = pd.read_sql_table('products', engine, columns=['product_id', 'quantity_in_stock', 'unit_price'])


#df = pd.read_sql_query("SELECT * FROM products", engine, index_col='product_id')

query = """
SELECT 
    productCode, 
    productName, 
    textDescription
FROM
    products t1
INNER JOIN productlines t2 
    ON t1.productline = t2.productline;
"""


df2 = pd.read_excel(r"Consumo_Cerveja.xlsx")
df2 = df2.drop(columns=["Unnamed: 7", "Unnamed: 8", "Unnamed: 9", "Unnamed: 10", "Unnamed: 11", "Unnamed: 12", "Unnamed: 13"])

# save into mysql
df2.to_sql(name = 'consumo_cerveja', con = engine, index = False) # if_exists = 'append' or if_exists = 'replace'

'''
# another way to connect to a database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='flavio123',
                             database='sql_novo',
                             )
c = connection.cursor()
c.execute("SELECT * FROM consumo_cerveja")
result = c.fetchone()
print(result)
'''
