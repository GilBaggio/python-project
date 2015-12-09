#number of boys and girls in all india level and total
"""
import logging
logger = logging.getLogger("fileerror")
logger.setLevel(logging.DEBUG)
fh=logging.FileHandler("logs\\fileerror.log")
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
"""

import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle, islice

def gender_count():
    try:
        #opening and reading the standardised data file
        stdfile = open("Standardiseddata.csv","r")
        firstline = stdfile.readline()
        heading = firstline.split(",")
        gender_index = heading.index("GENDER")
        
        #creating an empty list and count
        genderlist = []
        bcount = 0       #boys count
        gcount = 0      #girls count
        
        #iterating to append the gender index values
        for value in stdfile:
            data=value.split(",")
            genderlist.append(data[gender_index])      #adding the index to genderlist
        
        #iterating the boys and girls count
        for i in genderlist:
            if i == "Boy":
                bcount = bcount + 1
            else:
                gcount = gcount + 1
        totalstudent = bcount + gcount
    except IOError as e:
        print "Oops,something went wrong"
        print e.errno
        print e.strerror
    else:
        #print statements
        print "  ","Total_Boys","  ","Total_Girls","   ","Total_Students"
        print "   ",bcount,"\t  ",gcount,"\t  ",totalstudent
        
        count=[]
        #count1=[]
        #count2=[]
        count.append(bcount)
        count.append(gcount)
        count.append(totalstudent)
        
        plt.figure()
        #x= pd.DataFrame(count, columns=['one', 'two', 'three'])        
        x=pd.DataFrame(count)
        x.set_index([["Boys","Girls","Total"]],inplace=True)

        my_colors = list(islice(cycle(['y', 'r', 'g', 'y', 'k']),len(count)))        
        x.plot(kind="bar",width=0.1,color=my_colors,rot=0,legend=None)
        #x.legend("girls")
        plt.title("Total number of students")
        plt.xlabel("count")
        plt.ylabel("Gender")
        #plt.legend()
        
gender_count()
     


