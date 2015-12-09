#pass and fail percent in each state and rural/urban

def pass_fail():
    
    try:    
        #opening and reading the standerdised file
        stdfile = open("Standardiseddata.csv","r")
        firstline = stdfile.readline()
        heading = firstline.split(',')
        state_index = heading.index("state")
        percentage_index = heading.index("mathpcor")
        area_index = heading.index("AREA")
        #student=head.index("STUID")
        #gender=head.index("GENDER")
        
        state_name = raw_input("Enter the State Code: ").upper()          # enter different states
        area_name = raw_input("Enter the area type-\n Rural or Urban: ")       # enter Rural or Urban
        j=area_name[0]
        j=j.upper();
        area_name= area_name.replace(area_name[0], j, 1)
        #print area_name
        totalstucount = passcount = 0        #count2=count3=0
        
        #iterating statements
        for line in stdfile:
            data = line.split(',')
            if data[state_index] == state_name:       # different state name
                if data[area_index] == area_name:         # Rural or Urban
                    totalstucount = totalstucount + 1       # total students count       
                    if float(data[percentage_index]) >= 50:       # to find students above 50%
                        passcount = passcount + 1       # count of stucents passed in the area
        passper = float(passcount) / totalstucount * 100
        failper = float(100 - passper)
    except IOError as e:
        print "Oops,something went wrong"        
        print e.errno
        print e.strerror 

    else:        
        #print statement          
        print "Total_Student_area"," ","No_Of_Students_Passed"," ","Pass_Percentage","  ","Fail Percentage\n"
        print "   ",totalstucount,"                  ",passcount,"            ",passper,"      ",failper
