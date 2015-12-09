# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 16:41:56 2015

@author: tsc20
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statelist
statelist.state_codes()
def pass_percent_state():
    percent_details = {}
    file_content=open('Standardiseddata.csv','r')
    row1 = file_content.readline()
    head = row1.split(',')
    state_index = head.index('state')
    percentage_index = head.index('mathpcor')
    for element in statelist.state_list:
        count_student = 0
        count_pass = 0
        for record in file_content:
            data = record.split(',')
            if data[state_index] == str(element):
                count_student += 1
                if float(data[percentage_index]) >= 50:
                    count_pass += 1
        file_content.seek(0)
        percentage = float(count_pass)/count_student*100
        percent_details[element] = percentage
    plt.figure(figsize=(11,7))
    plt.bar(range(len(percent_details)), percent_details.values(),width=0.4)
    plt.xticks(range(len(percent_details)), percent_details.keys())
    #plt.xticks(range(1, len(labels)+1), labels, size='small')
    #index = np.arange(0, n_groups * 2, 2)
    plt.show()
pass_percent_state()
        
                        
