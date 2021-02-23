# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:50:58 2021

@author: gabre
"""

from twilio.rest import Client

client = Client(
    "API_ID", 
    "AUTH_CODE")

for msg in client.messages.list():
    print(f"Deleting {msg.body}")
    msg.delete()

# +18577073936
# +5521987327066 

'''
msg = client.messages.create(
    to="number_to",
    from_="number_from",
    body="Hello from Python"
    )


print(f"Created a new message: {msg.sid}")
'''
