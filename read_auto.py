# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 15:07:10 2021

@author: gabre
"""

#speaker.setProperty("voice", voices[2].id)  

import pyttsx3
import PyPDF2

arq = open("file_name.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(arq)

# How many pages
pages = pdfReader.numPages
print(pages) 

# Creating the speaker
speaker = pyttsx3.init()

# Loop
'''
page_start = 1
for num in range(page_start, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
'''

page = pdfReader.getPage(1)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()


#    See available voices
'''
voices = speaker.getProperty('voices')
for voice in voices:
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")
'''

'''
#    Get english version
speaker.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")  # Male
#speaker.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")   # Female         
speaker.setProperty("rate", 145)  # set speed
speaker.say(text)
speaker.runAndWait()
'''









