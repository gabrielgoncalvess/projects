# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:18:30 2021

@author: gabre
"""

from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title("Weather App")
root.geometry("365x200")
root.configure(background='white')
root.iconbitmap("W_logo.ico")

logo = ImageTk.PhotoImage(Image.open("WeatherApp.png"))

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=10028&distance=5&API_KEY=your_API_KEY

# Create Zipcode Lookup Function
def ziplookup():
    #zip.get()
    #zipLabel = Label(root, text=zip.get())
    #zipLabel.grid(row=1, column=0, columnspan=2)
    top = Toplevel()
    top.title("Second Window")
    
    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=your_API_KEY")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        
        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"
            
        top.configure(background=weather_color)
        
        
        myLabel = Label(top, text=city + "\n Air Quality: " + str(quality) + "\n" + category, font=("Helvetic", 30), background=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error"


zip = Entry(root, bg="light blue", fg="white", font=("Helvetic", 12))
zip.grid(row=1, column=0, sticky=W+E+N+S, padx=(10,0))

zip_btn = Button(root, text="Lookup Zipcode", command=ziplookup)
zip_btn.grid(row=1, column=1, sticky=W+E+N+S, padx=(0,20))

image_label = Label(image=logo)
image_label.grid(row=0, column=0, columnspan=2)


root.mainloop()
