"""highest scoreres in each difficulty level"""

import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle,islice

def high_difficulty_level():
    
    difficult=[]
    try:    
        
        #opening and reading the data file
        print("\nHighest Difficulty Level")
        print ""
        with open("high.csv","r") as datafile:
            firstline = datafile.readline()
            heading = firstline.split(",")
            percentage_index = heading.index('mathpcor')
            stud_ind = heading.index('STUID')
            high = []
            for line in datafile:
                data = line.split(",")
                if float(data[percentage_index]) >= 50:
                    high.append(float(data[percentage_index]))         # append the percentage_index to high 
                    maxhigh = max(high)       # take the max percentage among the high data
                    stud=data[stud_ind]
                    difficult.append(high)
            
    except IOError as e:
        print "Oops,something went wrong"                
        print e.errno
        print e.strerror  
    
    else:            
            print "Student ID "," ""Percentage "
            print stud,"  ",maxhigh
            print("\nMedium Difficulty Level")
            print ""
        
    try:  
        
        #opening and reading the data file
        with open("inter.csv","r") as datafile:
            firstline = datafile.readline()
            heading = firstline.split(",")
            percentage_index = heading.index('mathpcor')
            stud_ind = heading.index('STUID')
            medium = []
            for line in datafile:
                data = line.split(",")
                if float(data[percentage_index]) >= 50:
                    medium.append(float(data[percentage_index]))      # append the percentage_index to medium 
                    maxmedium = max(medium)       # take the max percentage among the medium data
                    stud=data[stud_ind]
                    difficult.append(medium)
    except IOError as e:        
        print "Oops,something went wrong"        
        print e.errno
        print e.strerror  
    
    else:          
            print "Student ID "," ","Percentage "
            print stud,"  ",maxmedium  
            print("\nLowest Difficulty Level")
            print ""

    try:        
        #opening and reading the data file
        with open("low.csv","r") as datafile:
            firstline = datafile.readline()
            heading = firstline.split(",")
            percentage_index = heading.index('mathpcor')
            stud_ind = heading.index('STUID')
            low = []
            for line in datafile:
                data = line.split(",")
                low.append(float(data[percentage_index]))      # append the percentage_index to low 
                maxlow = max(low)         # take the max percentage among the low data    
                stud=data[stud_ind]
                difficult.append(low)
            
    except IOError as e:        
        print "Oops,something went wrong"                
        print e.errno
        print e.strerror  
    
    else:            
            print "Student ID "," ","Percentage "
            print stud,"  ",maxlow 
            print("\nRemaining Category")
            print ""

    try:     
        #opening and reading the data file
        with open("rem.csv","r") as datafile:
            firstline = datafile.readline()
            heading = firstline.split(",")
            percentage_index = heading.index('mathpcor')
            stud_ind = heading.index('STUID')
            remain = []
            for line in datafile:
                data = line.split(",")
                remain.append(float(data[percentage_index]))      # append the percentage_index to remain 
                maxrem = max(remain)        # take the max percentage among the remain data    
                stud=data[stud_ind]
                difficult.append(remain)                
            
    except IOError as e:        
        print "Oops,something went wrong"                
        print e.errno
        print e.strerror  
    
    else:
            print "Student ID "," ","Percentage "
            print stud,"  ",maxrem   
            
            plt.figure()
            pd.set_option('max_columns',7)
            x = pd.DataFrame(difficult,columns = ['count'])
            x.set_index([['HDL','IL','LL','REM']],inplace = True)
            
           
            '''plt.set_xlabels("States")           
            plt.set_ylabels("pass Percentage")
            ax.set_xticklabels("Pass")'''
            
            my_colors = list(islice(cycle(['y','g','r','c']),None,len(difficult)))
            x.plot(kind = "bar",width = 0.6,rot = 0,color = my_colors)
            plt.title('Highest scorers in difficult levels')
            plt.xlabel('Difficulty Levels')
            plt.ylabel('Percentage')
            
            
    
    

    
high_difficulty_level()
          
    
