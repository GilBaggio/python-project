#importing file definitions

import Filedefinition
Filedefinition.Filedefinition()

#writing onto a new file after standerdisation
formattedfile = open("Standardiseddata.csv",'w')
formattedfile.write(Filedefinition.firstline)
stateindex = Filedefinition.heading.index('state')

#iterating each line in the original csv file
for line in Filedefinition.f:
    data = line.split(',')
    string = data[stateindex]
    length_string = len(string)
    newstring = ''
    
    #iterating each state index value
    for i in range(length_string):
        if('A' <= string[i] <= 'Z'):
            newstring = newstring+string[i]
            data[stateindex] = newstring
            
    #adding comma values to each line
    line = ",".join(data)
    formattedfile.write(line)
Filedefinition.f.close()
formattedfile.close()
    
    
