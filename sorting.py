stdfile = open("Standardiseddata.csv","r")
firstline = stdfile.readline()
heading=firstline.split(",")
percentage_index=heading.index("mathscl")
#opening seperate files for each category
hfile=open("high.csv","w")
ifile=open("inter.csv","w")
lfile=open("low.csv","w")
rfile=open("rem.csv","w")
hfile.write(firstline)
ifile.write(firstline)
lfile.write(firstline)
rfile.write(firstline)

#iterating statements with conditions
for line in stdfile:
    data=line.split(",")
    if float(data[percentage_index])>=226 and float(data[percentage_index])<230:
        lfile.write(line)       # check the condition and store it in lfile(low file)
    elif float(data[percentage_index])>=230 and float(data[percentage_index])<275:
        ifile.write(line)       # check the condition and store it in ifile(intermediate file)
    elif float(data[percentage_index])>275:
        hfile.write(line)       # check the condition and store it in hfile(high file)
    else:
        rfile.write(line)       # rfile(remaining file)
hfile.close()
ifile.close()
lfile.close()
rfile.close()
