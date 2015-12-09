def Filedefinition():
    #global definitions
    global f
    global firstline
    global heading

    
    f=open('C8NAS_MATH.csv','r')
    firstline=f.readline()
    heading=firstline.split(",")
