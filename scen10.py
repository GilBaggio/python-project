#highest scoreres in each difficulty level

def high_difficulty_level():
    
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
                high.append(data[percentage_index])         # append the percentage_index to high 
                maxhigh = max(high)       # take the max percentage among the high data
                if float(data[percentage_index]) >= maxhigh:
                    print maxhigh
                
                
    except IOError as e:
        print "Oops,something went wrong"                
        print e.errno
        print e.strerror  
    
    else:            
            print "Student ID "," ""Percentage "
            print data[stud_ind],"  ",maxhigh
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
                    medium.append(data[percentage_index])       # append the percentage_index to medium 
                    maxmedium = max(medium)       # take the max percentage among the medium data
            
    except IOError as e:        
        print "Oops,something went wrong"        
        print e.errno
        print e.strerror  
    
    else:          
            print "Student ID "," ","Percentage "
            print data[stud_ind],"  ",maxmedium  
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
                low.append(data[percentage_index])      # append the percentage_index to low 
                maxlow = max(low)         # take the max percentage among the low data    
            
    except IOError as e:        
        print "Oops,something went wrong"                
        print e.errno
        print e.strerror  
    
    else:            
            print "Student ID "," ","Percentage "
            print data[stud_ind],"  ",maxlow 
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
                remain.append(data[percentage_index])       # append the percentage_index to remain 
                maxrem = max(remain)        # take the max percentage among the remain data    
    except IOError as e:        
        print "Oops,something went wrong"                
        print e.errno
        print e.strerror  
    
    else:
            print "Student ID "," ","Percentage "
            print data[stud_ind],"  ",maxrem
            
high_difficulty_level();
          
    
