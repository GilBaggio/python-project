#list of all mediums and count

def med_list():

    try:    
        medium = []
        total = [0,1,2,3,4,5,6,7,8,9,10]      # list to store total no of students
        boys = [0,0,0,0,0,0,0,0,0,0,0]        # list to store total no of boys
        girls = [0,0,0,0,0,0,0,0,0,0,0]       # list to store total no of girls
    
        #opening an reading a standerdised file
        stdfile = open('Standardiseddata.csv',"r")
        firstline = stdfile.readline()
        heading = firstline.split(",")
        medium_index = heading.index('medium')
        #percentage = heading.index("mathpcor")
        gender_index = heading.index("GENDER")
    
        count = count0 = count1 = count2 = count3 = count4 = count5 = count6 = count7 = count8 = count9 = count10 = count11 = count12 = count13 = count14 = count15 = count16 = count17 = count18 = count19 = count20 = count21 = count22 = count23 = count24 = count25 = count26 = count27 = count28 = count29 = count30 = count31 = count32 = 0
        print heading[medium_index],"         ","Total","   ","Boys","   ","Girls","\n"
        
        #iterating statements
        for line in stdfile:
            data = line.split(',')
            medium.append(data[medium_index])
    
            #condition statements
            if data[medium_index] == "Bengali":       # checking the medium 
                count = count + 1       # if the medium is checked count the students
                total[0] = count      # store the count to the total(list)
                if data[gender_index] == "Boy":       # checking the gender boy 
                    count11 += 1       # if the gender is checked count the boy
                    boys[0] = count11         # store the count to the boys(list)
                elif data[gender_index] == "Girl":
                    count12 += 1
                    girls[0] = count12
    
            elif data[medium_index] == "English":
                count1 = count1 + 1
                total[1] = count1
                if data[gender_index] == "Boy":
                    count13 += 1
                    boys[1] = count13
                elif data[gender_index] == "Girl":
                    count14 += 1
                    girls[1] = count14
    
            elif data[medium_index] == "Gujarati":
                count2 = count2 + 1
                total[2] = count2
                if data[gender_index] == "Boy":
                    count15 += 1
                    boys[2] = count15
                elif data[gender_index] == "Girl":
                    count16 += 1
                    girls[2] = count16
                
            elif data[medium_index] == "Hindi":
                count3 = count3 + 1
                total[3] = count3
                if data[gender_index] == "Boy":
                    count17 += 1
                    boys[3] = count17
                elif data[gender_index] == "Girl":
                    count18 += 1
                    girls[3] = count18
                    
            elif data[medium_index] == "Kannada":
                count4 = count4 + 1
                total[4] = count4
                if data[gender_index] == "Boy":
                    count19 += 1
                    boys[4] = count19
                elif data[gender_index] == "Girl":
                    count20 += 1
                    girls[4] = count20
                    
            elif data[medium_index] == "Malayalam":
                count5 = count5 + 1
                total[5] = count5
                if data[gender_index] == "Boy":
                    count21 += 1
                    boys[5] = count21
                elif data[gender_index] == "Girl":
                    count22 += 1
                    girls[5] = count22
            elif data[medium_index] == "Marathi":
                count6 = count6 + 1
                total[6] = count6
                if data[gender_index] == "Boy":
                    count23 += 1
                    boys[6] = count23
                elif data[gender_index] == "Girl":
                    count24 += 1
                    girls[6] = count24
                    
            elif data[medium_index] == "Oriya":
                count7 = count7 + 1
                total[7] = count7
                if data[gender_index] == "Boy":
                    count25 += 1
                    boys[7] = count25
                elif data[gender_index] == "Girl":
                    count26 += 1
                    girls[7] = count26
                    
            elif data[medium_index] == "Punjabi":
                count8 = count8 + 1
                total[8] = count8
                if data[gender_index] == "Boy":
                    count27 += 1
                    boys[8] = count27
                elif data[gender_index] == "Girl":
                    count28 += 1
                    girls[8] = count28
                    
            elif data[medium_index] == "Tamil":
                count9 = count9 + 1
                total[9] = count9
                if data[gender_index] == "Boy":
                    count29 += 1
                    boys[9] = count29
                elif data[gender_index] == "Girl":
                    count30 += 1
                    girls[9] = count30
            elif data[medium_index] == "Telugu":
                count10 = count10 + 1
                total[10] = count10
                if data[gender_index] == "Boy":
                    count31 += 1
                    boys[10] = count31
                elif data[gender_index] == "Girl":
                    count32 += 1
                    girls[10] = count32
        
        medium = set(medium)            # converting the medium list into set and again store it to medium
        medium = list(sorted(medium))       # medium is again converted to list and display in sorted format
        lenmed = len(medium)        # taking the length of medium 
                 # medium count
            
    except IOError as e:        
        print "Oops,something went wrong"                
        print e.errno
        print e.strerror 
            
    else:
        for totaleve in range(lenmed):      
            count0 += 1
            print "%7s%14d%7d%7d"%(medium[totaleve],total[totaleve],boys[totaleve],girls[totaleve])
        print "\nTotal number of medium: ",count0
    

