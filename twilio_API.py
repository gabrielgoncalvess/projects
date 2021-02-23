# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:50:58 2021

@author: gabre
"""

from twilio.rest import Client

client = Client(
    "ACcf85dc43741e9a83b53992b2a3986ab9", 
    "b3e8a684d15301e806476a6ecea1f082")

for msg in client.messages.list():
    print(f"Deleting {msg.body}")
    msg.delete()

# +18577073936
# +5521987327066 

'''
msg = client.messages.create(
    to="+5521987327066",
    from_="+18577073936",
    body="Hello from Python"
    )


print(f"Created a new message: {msg.sid}")
'''