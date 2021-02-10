# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 00:14:52 2021

@author: gabre
"""

from graphviz import Source
path = "music-recommender.dot"
s = Source.from_file(path)
s.view()
