"""list of states and count of states"""

import matplotlib.pyplot as plt
import pylab
def state_count():
    
    try:
        #opening and reading the standardised data file
        stdfile = open("Standardiseddata.csv","r")
        firstline = stdfile.readline()
        heading=firstline.split(",")
        state_index=heading.index("state")
        
        #creating an empty list
        statelist=[]
        final=[]
        #print heading[state_index]      #print the state name
            
        #iterating statements
        for line in stdfile:
            data=line.split(",")
            statelist.append(data[state_index])     #adding the state_index to statelist
        statevalue=set(statelist)       #creating a set to avoid duplicate values
        final=list(statevalue)      # changing the set to list
        print "Total number of states which participated in the assesment: ",len(final)                
        print heading[state_index]      #print the state name        
        for stateco in final:
            print stateco      #printing the state name
    
    except IOError as e: 
        print "Oops,something went wrong"
        print e.errno
        print e.strerror    
    
    #else:    
        #print statement
state_count()
