# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 16:45:57 2015

@author: tsc20
"""

def state_codes():
    global state_list
    file_content=open('Standardiseddata.csv','r')
    row1 = file_content.readline()
    head = row1.split(',')
    state_index = head.index('state')
    state_list = []
    state_set = set({})
    for record in file_content:
        data = record.split(',')
        state_set.add(data[state_index])
        state_list = list(state_set)
            
