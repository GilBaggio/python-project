# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 09:59:46 2015

@author: tsc17
"""

#highest scoreres in each difficulty level

def high_difficulty_level():   
        #opening and reading the data file
        print("\nHighest Difficulty Level")
        print ""
        with open("high.csv","r") as datafile:
            firstline = datafile.readline()
            heading = firstline.split(",")
            percentage_index = heading.index('mathpcor')
            stud_ind = heading.index('STUID')
            high = []
            count=0            
            for line in datafile:
                data = line.split(",")
                high.append(float(data[percentage_index]))         # append the percentage_index to high 
                maxhigh = max(high)
            print maxhigh
            """if float(data[percentage_index])== float(maxhigh):
                    count +=1
                print count"""
            #print high
            #datafile.seek(0)    
            for i in high:
                if i==maxhigh:
                    count +=1
            print count
                # take the max percentage among the high data
            
            
            """for line in datafile:
                row=line.readline()
                data = row.split(",")
                if float(data[percentage_index]) == float(maxhigh):
                    count += 1
                    #print "Student ID "," ""Percentage "
            print count """       #print data[stud_ind],"  ",maxhigh   
high_difficulty_level();