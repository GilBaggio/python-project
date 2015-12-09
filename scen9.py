#Highest percentage in all india level

def high_percentage():
    
    try:
        
        #opening and reading the standerdised file
        stdfile = open('Standardiseddata.csv','r')
        firstline = stdfile.readline()
        heading = firstline.split(',')
        percentage_index = heading.index('mathpcor')
        studentid_index = heading.index('STUID')
        state_index = heading.index('state')
        percentagelist = []
        higher = 0
    
        #iterating statements
        for line in stdfile:
            data = line.split(',')
            if data[percentage_index] > higher:       # check the percentage with the condition
                higher = data[percentage_index]       # add the highest percentage and check with other
                percentagelist = data         # move the highest data to the percentagelist
            else:
               higher = higher
               
    except IOError as e:
        print "Oops,something went wrong"        
        print e.errno
        print e.strerror

    else:               
        print "Highest_Scorer_ID","  ","Percentage","  ","State_Name\n"
        print " ",percentagelist[studentid_index],"       ",percentagelist[percentage_index],"        ",percentagelist[state_index]
