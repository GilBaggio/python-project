"""students who scored above 90"""

def higher_level():
    
    try:
        #opening and reading the standardised data file
        stdfile = open("Standardiseddata.csv","r")        #opening the standardised file
        firstline = stdfile.readline()        #read the firstline in data file
        heading = firstline.split(",")        #splitting the heading         
        studentid_index = heading.index("STUID")       #finding the index of studid
        state_index = heading.index("state")        #finding the index of state
        district_index = heading.index("DIST")      #finding the index of district
        percentage_index = heading.index("mathpcor")        #finding the index of mathpcor
        
        #print statements
        print "",heading[studentid_index],"     ",heading[state_index],"   ",heading[district_index],"   ",heading[percentage_index]
        
        #iterating statements
        for line in stdfile:
            data = line.split(",")
            if float(data[percentage_index]) > 90:        #checking the percentage_index who have scored above 90%
                #print statements
                print data[studentid_index],"  ",data[state_index],"     ",data[district_index],"       ",data[percentage_index]
    
    except IOError as e:
        print "Oops,something went wrong"        
        print e.errno
        print e.strerror  

        
