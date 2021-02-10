# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:12:03 2021

@author: gabre
"""

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)
            
folder_to_track = r"C:\Users\gabre\Desktop\myFolder"
folder_destination = r"C:\Users\gabre\Desktop\newFolder"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()


try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()