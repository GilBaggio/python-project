import Filedefinition
def StateWisePass():
 
    total,count=0,0;
    Filedefinition.Filedefinition()
    score=Filedefinition.heading.index("mathscl")
    for line in Filedefinition.f:
        count+=1
        data=line.split(",")
        if(float(data[score])>250):
            total+=float(data[score])        
    Pass=(total/(count*500))*100
    Fail=100-Pass
    print Pass
    print Fail

    Filedefinition.f.close()
StateRuralWise()                
