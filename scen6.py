#display the student who got the highest percentage in a state

def state_high():
    
    try:
        #opening and reading the standardised data file
        stdfile = open("Standardiseddata.csv","r")
        firstline = stdfile.readline()
        heading = firstline.split(',')
        state_index = heading.index("state")
        percentage_index = heading.index("mathpcor")
        studentid_index = heading.index("STUID")
        
        state_name = raw_input("Enter the State Code: ").upper()        #enter the different states
        print ""
        statelist = []
        perhigh = 0
        
        #iterating statements
        for line in stdfile:
            data = line.split(',')
            if data[state_index] == state_name:     # matching the state name
                if data[percentage_index] > perhigh:      # check the percentage with the condition     
                    perhigh = data[percentage_index]      
                    statelist = data      # storing the particular student data in a list
    except IOError as e: 
        print "Oops,something went wrong"
        print e.errno
        print e.strerror 

    else:                    
        #print statement
        print "STUDENT_ID","  ","Percentage"
        print statelist[studentid_index],"  ",statelist[percentage_index]

