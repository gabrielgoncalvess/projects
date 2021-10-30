# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 23:07:51 2021

@author: Gabriel
"""

from selenium import webdriver
import urllib.request
import zipfile
import os
from bs4 import BeautifulSoup
import requests
import re

# This program checks if the chromedriver version is the same as
# Chrome version. Otherwise, it downloads the correct one.

def test_webdriver():
    try:
        PATH = ('chromedriver.exe')
        driver = webdriver.Chrome(PATH)
        if 'browserVersion' in driver.capabilities:
            chrome_version = driver.capabilities['browserVersion']
        else:
            chrome_version = driver.capabilities['version']
        driver_version = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
        driver.quit()
    except Exception as e:
        msg = e.msg
        regexp = re.compile(r'[\d.]*\d+')
        version_support, current = regexp.findall(msg)

        page_url = 'https://chromedriver.chromium.org/downloads'
        
        page = requests.get(page_url)
        
        soup = BeautifulSoup(page.text, 'html.parser')
        
        dl_list = soup.find_all('a',{'class':'XqQF9c'})[0:3]
        
        right_v = (x['href'] for x in dl_list if current.split('.')[0]
                        == regexp.findall(x['href'])[0].split('.')[0])
        
        right_version = regexp.findall(next(right_v))[0]

        dl_link = f"https://chromedriver.storage.googleapis.com/{right_version}/chromedriver_win32.zip"
        
        with urllib.request.urlopen(dl_link) as dl_file:
            with open('chromedriver_win32.zip', 'wb') as out_file:
                out_file.write(dl_file.read())
            os.remove('chromedriver.exe')
            with zipfile.ZipFile('chromedriver_win32.zip', 'r') as zip_ref:
                zip_ref.extractall()
            os.remove('chromedriver_win32.zip')