#head counts in each difficulty level

def head_count():
    
    try:    
        #opening and reading the data file
        dfile = open("high.csv","r")
        #high=dfile.readline()
        high_row_count = sum(1 for line in dfile)
        print "Number of students who passed the high difficulty level: ",high_row_count
        dfile.close()
    
        #opening and reading the file
        dafile = open("inter.csv","r")
        #inter=dafile.readline()
        inter_row_count = sum(1 for line in dafile)
        print "Number of students who passed the medium difficulty level: ",inter_row_count
        dafile.close() 
    
        #opening and reading the file
        datfile = open("low.csv","r")
        #low=datfile.readline()
        low_row_count = sum(1 for line in datfile)
        print "Number of students who passed the low difficulty level: ",low_row_count
        datfile.close()
    
        #opening and reading the file
        datafile = open("rem.csv","r")
        #rem=datafile.readline()
        rem_row_count = sum(1 for line in datafile)
    
    except IOError as e:
        print "Oops,something went wrong"        
        print e.errno
        print e.strerror 
    
    else:
        print "Number of students who have failed: ",rem_row_count
