# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:05:06 2021

@author: gabre
"""

import os
import tweepy as tw
import pandas as pd

# Twitter API
consumer_key = 'QDLIVaDcozHczwGJKIPimO3DZ'
consumer_secret = 'GK4XheEkf94PKiLaZcQBIxUb3VV1c2PKAjRIPF3Geoq6PmLd2V'
token = '1346543793009545216-j1NFVxNWTUMrGbVHnlvAfDBq2peNo4'
token_secret = 'ZWSk424OsrHXHMFQtrCrooZARLZK1nkEsrDbTshe3C5iu'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token, token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define o intervalo de tempo para busca de tweets
from datetime import date, timedelta

delta = timedelta(days=60)        # Intervalo para busca
start_date = date.today()        # data de hoje
start_date -= delta
search_term = "bradesco"
limit = 2000

# Inicializa dataframe vazio para salvar todos os tweets
col_names =  ["date", "tweet", "username", "retweet", "nlikes", "nreplies", "nretweets", "near"]
tweets_dataframe  = pd.DataFrame(columns = col_names)

# define intervalo de datas   
date_string = start_date.strftime("%Y-%m-%d")

# busca tweets no intervalo definido
tweets = tw.Cursor(api.search, q=search_term, lang="pt", since=start_date).items(limit)
tweets_info = [[tweet.created_at, tweet.text, tweet.user.screen_name, tweet.retweeted, tweet.favorite_count, tweet.in_reply_to_status_id, tweet.retweet_count, tweet.user.location] for tweet in tweets]

# Extrai um dataframe
df = pd.DataFrame(data=tweets_info, columns=col_names)


df.to_excel('tweets.xlsx', index=False, encoding="utf-8")


