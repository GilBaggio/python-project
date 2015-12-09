"""state wise pass percentage """

import pandas as pd
import matplotlib.pyplot as plt
#from itertools import islice,cycle
def state_pass():
    
    try:
        #opening and reading the standardised data file
        stdfile = open("Standardiseddata.csv","r")
        firstline = stdfile.readline()
        heading = firstline.split(',')
        state_index = heading.index("state")
        percentage_index = heading.index("mathpcor")
        gender_index = heading.index("GENDER")
        state_name = raw_input("Enter the State Code: ").upper()      #different states
        scount = spcount = bpcount = gpcount = 0        #count for studends,students passed,pass percentage,boys passed,girls passed
        
        x=[]
        #y=[]
        z=[]
        pass_list=[]
        #iterating statements
        for line in stdfile:
            data = line.split(',')
            if data[state_index] == state_name:       #matching the state name
                scount += 1 #students count
                if float(data[percentage_index]) >= 50:     #scored above 50%
                    spcount = spcount + 1       #no of students passed
                    if data[gender_index] == "Boy":
                        bpcount = bpcount + 1       #no of boys passed
                    else:
                        gpcount = gpcount + 1       #no of girls passed
              
        pass_percentage = float(spcount) / scount * 100         #pass percentage for the particular state
        fail_percentage=float(100-float(pass_percentage))
        x.append(scount)
        x.append(spcount)
        z.append(pass_percentage)
        z.append(fail_percentage)
        pass_list.append(bpcount)
        pass_list.append(gpcount)
        
    except IOError as e:
        print "Oops,something went wrong"        
        print e.errno
        print e.strerror  

    else:        
        #print statements           
        print "Students_In_STATE","Students_Passed","Pass_Percentage","Boys_Passed","Girls_Passed"
        print scount,"              ",spcount,"      ","   ",pass_percentage,"   ",bpcount,"       ",gpcount
        #print x
        #print y
        #z=zip(x,y)
        
        labels = 'Boys', 'Girls',
        #sizes = [15, 30, 45, 10]
        colors = ['yellowgreen', 'gold']
        explode = (0, 0) # only "explode" the 2nd slice 

        plt.pie(pass_list, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
        # Set aspect ratio to be equal so that pie is drawn as a circle.
        plt.axis('equal')
        plt.title("******* Gender Ratio *******")
        #plt.show()
        
        
        plt.subplot()
        df=pd.DataFrame(x)
        df.set_index([["Total students in state","students passed"]],inplace=True)
        bar_color=["cyan","r"]
        df.plot(kind="bar",rot=0,legend=None,color=bar_color)
        plt.title("Total students and students passed")
        plt.xlabel("Student")
        plt.ylabel("count")
        
        
        
        
    
state_pass();