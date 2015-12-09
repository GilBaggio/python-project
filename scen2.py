#number of students who got the maximum score in all india level and the max score

import pandas as pd
import matplotlib.pyplot as plt
from itertools import islice,cycle

def max_score():
    
    try:
        #opening and reading the data file
        datafile = open("high.csv","r")         #opening the data file
        firstline = datafile.readline()         #read the firstline in data file
        heading = firstline.split(",")          #splitting the heading
        mathscl_index = heading.index("mathscl")    #finding the index
        
        #creating an empty list
        scorelist = []
        maxcount = 0
        
        #iterating statements
        for value in datafile:
            data = value.split(",")
            scorelist.append(data[mathscl_index])       #adding the mathscl_index to scorelist
        for scorelistvalue in scorelist:
            if scorelistvalue == max(scorelist):       #finding the maximum score
                maxcount = maxcount + 1     #count of maximum score
    except IOError as e:
        print "Oops,something went wrong"        
        print e.errno
        print e.strerror
    
    else:
        #print statements
        print "Highest_score_in_India ","No_of_student_got_First_Rank_in_India \n"
        print " ",max(scorelist),"\t\t\t",maxcount
        
        #count=[]
        maxscore=[]
        maxscore.append(float(max(scorelist)))
        maxscore.append(maxcount)
        #print count
        
        plt.figure()
        x=pd.DataFrame(maxscore)
        x.set_index([["maximum score","no of students"]],inplace=True)
        my_color = list(islice(cycle(["g","r"]),None,len(maxscore)))
        x.plot(kind="Bar",width=0.2,rot=0,legend=None,color=my_color)
        plt.title("Highest score in all india level and the count")
        plt.xlabel("Legend")
        plt.ylabel("Score")
max_score();

