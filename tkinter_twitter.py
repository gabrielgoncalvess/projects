# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 19:43:23 2021

@author: gabre
"""

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import os
import tweepy as tw
import pandas as pd
from datetime import date, timedelta

root = Tk()
root.title("Twitter Database")
root.iconbitmap("twitter_ico.ico")

#root.configure(background='black')
#root.geometry("400x600")

#.resize((200,200), Image.ANTIALIAS))


logo = ImageTk.PhotoImage(Image.open("twitter_logo.png").resize((200,200), Image.ANTIALIAS))

image_label = Label(image=logo)
image_label.grid(row=0, column=0, columnspan=2)


#Labels

consumer_key_label = Label(root, text="Consumer Key")
consumer_key_label.grid(row=1, column=0, pady=(10,0))

consumer_secret_label = Label(root, text="Consumer Secret")
consumer_secret_label.grid(row=2, column=0)


token_label = Label(root, text="Token")
token_label.grid(row=3, column=0)

token_secret_label = Label(root, text="Token Secret")
token_secret_label.grid(row=4, column=0)

#start_date_label = Label(root, text="Start Date")
#start_date_label.grid(row=6, column=0, pady=(20,0))

interval_label = Label(root, text="Interval (in days)")
interval_label.grid(row=8, column=0, pady=(20,0))

search_term_label = Label(root, text="Search Term")
search_term_label.grid(row=9, column=0)

limit_label = Label(root, text="Number of Tweets")
limit_label.grid(row=10, column=0)

language_label = Label(root, text="Language (en, pt...)")
language_label.grid(row=11, column=0)

def create():
    # Twitter API
    consumer_key = consumer_key_E.get()
    consumer_secret = consumer_secret_E.get()
    token = token_E.get()
    token_secret = token_secret_E.get()
    
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token, token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    
    # Interval for search

    delta = timedelta(days=int(interval_E.get()))        # Interval
    start_date = date.today()        # today
    start_date -= delta
    search_term = search_term_E.get()
    limit = int(limit_E.get())
    langg = language_E.get()
    
    
    # Creates an empty dataframe
    col_names =  ["date", "tweet", "username", "retweet", "nlikes", "nreplies", "nretweets", "near"]
    tweets_dataframe  = pd.DataFrame(columns = col_names)
    
    #date_string = start_date.strftime("%Y-%m-%d")
    
    # search for tweets
    tweets = tw.Cursor(api.search, q=search_term, lang=langg, since=start_date).items(limit)
    tweets_info = [[tweet.created_at, tweet.text, tweet.user.screen_name, tweet.retweeted, tweet.favorite_count, tweet.in_reply_to_status_id, tweet.retweet_count, tweet.user.location] for tweet in tweets]
    
    # creates de excel file
    df = pd.DataFrame(data=tweets_info, columns=col_names)
    df.to_excel('tweets.xlsx', index=False, encoding="utf-8")
    
    response = messagebox.showinfo("Created", "Excel File Created")
    return
 

# Entrys

consumer_key_E = Entry(root, width=30)
consumer_key_E.grid(row=1, column=1, padx=20, pady=(10,0))
consumer_secret_E = Entry(root, width=30)
consumer_secret_E.grid(row=2, column=1)
token_E = Entry(root, width=30)
token_E.grid(row=3, column=1)
token_secret_E = Entry(root, width=30)
token_secret_E.grid(row=4, column=1)
#start_date_E = Entry(root, width=30)
#start_date_E.grid(row=6, column=1, pady=(20,0))
interval_E = Entry(root, width=30)
interval_E.grid(row=8, column=1, pady=(20,0))
search_term_E = Entry(root, width=30)
search_term_E.grid(row=9, column=1)
limit_E = Entry(root, width=30)
limit_E.grid(row=10, column=1)
language_E = Entry(root, width=30)
language_E.grid(row=11, column=1)

create_btn = Button(root, text="Create Excel File", 
                    activebackground='black', activeforeground='white', bd=4, font="Helvetic", command=create)
create_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=143)





mainloop()